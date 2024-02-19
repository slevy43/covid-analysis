import csv

# individual list maker and wraps it into the dictionary
def dict_maker(filename):
    """
    Creates and returns a dictionary of dates and makes a list of all the cases for each date. The cases are tuples
    containing the patient's gender [1], age [2], and location [3]. If the current date ([0]) isn't in the dictionary,
    it makes an entry as a list with the current case in it. If the current date is in the dictionary, it appends the
    current case tuple onto the existing list. After each key is checked, it returns the dictionary.
    :param filename: The name of the csv file that the user is making this dictionary with
    :return: The dictionary of dates with their corresponding cases.
    """
    week_dict = {}      # dictionary that will contain the lists of tuples
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)                                            # skip the row containing the headers
        for row in reader:                                      # for each case in the csv file
            if row[0] in week_dict:                             # if its date is in the dictionary
                week_dict[row[0]].append((row[1], row[2], row[3]))
            else:                                               # if its date is not in the dictionary
                week_dict[row[0]] = [(row[1], row[2], row[3])]  # new key is date, value is list with current case
    return week_dict

def count_by_location(case_dict):
    """
    Finds the amount of cases per location. Loops through each case of each date and increments the location
    counter depending on what location the case contains.
    :param case_dict: Dictionary of each week's start date and its corresponding list of cases
    :return: Tuple containing case counts for London, Middlesex, and other locations
    """
    london_counter = 0                                # counters for each location
    middlesex_counter = 0
    other_counter = 0
    for key in case_dict:                             # for each date in the dictionary
        for group in case_dict[key]:                  # for each case of the current date
            if group[2] == 'City of London':          # Checking match for the 3rd item (County)
                london_counter += 1                   # increment London counter
            elif group[2] == 'Middlesex County':      # same for Middlesex as London
                middlesex_counter += 1
            else:                                     # Increment 'other' if not London or MS
                other_counter += 1
    total = (london_counter, middlesex_counter, other_counter)
    return total

def count_by_age_group(case_dict):
    """
    Finds the amount of cases per age group. Loops through each case of each date and increments the age group
    counter depending on what age-range the case falls under.
    :param case_dict: Dictionary of each week's start date and its corresponding list of cases
    :return: Tuple containing case counts for under 40, 40-80, and 80+ groups
    """
    under_40 = 0                           # counters for each age group
    forty_80 = 0
    over_80 = 0
    for key in case_dict:                    # for each date in the dictionary
        for group in case_dict[key]:         # for each case of the current date
            if group[1] == '0-19':           # Checking match for the 2nd item (Age)
                under_40 += 1                # Incrementing if in certain range
            if group[1] == '20-29':          # Under 40 age ranges
                under_40 += 1
            if group[1] == '30-39':
                under_40 += 1
            if group[1] == '40-49':          # 40 to 80 age ranges
                forty_80 += 1
            if group[1] == '50-59':
                forty_80 += 1
            if group[1] == '60-69':
                forty_80 += 1
            if group[1] == '70-79':
                forty_80 += 1
            if group[1] == '80+':            # Over 80 age ranges
                over_80 += 1
    cases_by_age_group = (under_40, forty_80, over_80)
    return cases_by_age_group

def peak_case_count(case_dict):
    """
    Finds the date with the highest case count. Finds the amount of cases for each date. Makes a list of those
    amounts. Then checks the count dictionary for which date matches the highest case amount.
    :param case_dict: Dictionary of each week's start date and its corresponding list of cases
    :return: The date (as a string) which contains the most cases
    """
    count_dict = {}                         # start empty dictionary
    for key in case_dict:                   # for each key in the case dictionary
        length = len(case_dict[key])        # store the amount of cases for each date
        count_dict[key] = length            # make dictionary of dates (k) and amount of cases (v)
    case_count = list(count_dict.values())  # make list from value (amount of cases) of each date
    case_count.sort()                       # sorts case counts from lowest to highest
    for key in count_dict:
        if count_dict[key] == case_count[-1]:   # finding which date the highest count corresponds to
            return key                          # return the date of what matches the highest count

def cases_by_age_by_date(case_dict, highest_date):
    """
    Finds the amount of cases per age group on the date with the highest cases. Loops through each case of on
    the specific date and increments the age group counter depending on what age-range the case falls under.
    :param case_dict: Dictionary of each week's start date and its corresponding list of cases
    :param highest_date: String containing date with the highest cases
    :return: Tuple containing case counts for under 40, 40-80, and 80+ groups, for the given date
    """
    under_40 = 0                           # starting counters for age groups
    forty_80 = 0
    over_80 = 0
    for info in case_dict[highest_date]:   # traversing the tuples from the highest case count week
        if info[1] == '0-19':              # incrementing under 40 for ages that fall in range
            under_40 += 1
        if info[1] == '20-29':
            under_40 += 1
        if info[1] == '30-39':
            under_40 += 1
        if info[1] == '40-49':             # incrementing 40-80 for ages that fall in range
            forty_80 += 1
        if info[1] == '50-59':
            forty_80 += 1
        if info[1] == '60-69':
            forty_80 += 1
        if info[1] == '70-79':
            forty_80 += 1
        if info[1] == '80+':                # incrementing over 80 for ages that specify over 80
            over_80 += 1
    cases_by_age = (under_40, forty_80, over_80)
    return cases_by_age

def main():
    """
    Asks user to choose a csv file where each row is a case containing its date and the patients gender, age,
    and location. This function uses that information to write a file which gives a formatted breakdown of the
    information by location, age, and the highest date, with the age breakdown for that day.
    These formatted lines are then printed.
    """
    try:
        chosen_file = input('Which file would you like to analyze?\n')
        week_dict = dict_maker(chosen_file)
    # (london, MS, unknown)
        location = count_by_location(week_dict)
    # date of week with most cases
        highest_week = peak_case_count(week_dict)
    # for date: (under_40, forty_80, over_80)
        by_age_by_date = cases_by_age_by_date(week_dict, highest_week)
    # (under_40, forty_80, over_80)
        by_age_group = count_by_age_group(week_dict)
# writing time
        out_file = open("output/diagnosed_data.txt", "w")
    # 1st BLOCK
        out_file.write(f'There were {sum(location)} MLHU cases in total.\n')
        out_file.write(f'Of those, there were {location[0]} cases reported in London.\n')
        out_file.write(f'There were {location[1]} cases reported in Middlesex County.\n')
        out_file.write(f'There were {location[2]} cases reported from an unknown location.\n\n')
    # 2nd BLOCK
        out_file.write(f'Overall cases by age group:\n')
        out_file.write(f'People under 40 accounted for {by_age_group[0]} case(s).\n')
        out_file.write(f'People between 40 and 80 accounted for {by_age_group[1]} case(s)\n')
        out_file.write(f'People over 80 accounted for {by_age_group[2]} case(s).\n\n')
    # 3rd Block
        out_file.write(f'The most cases occurred on {highest_week}.\n')
        out_file.write(f'On that date, there were {sum(by_age_by_date)} cases, broken down by age as follows:\n')
        out_file.write(f'{by_age_by_date[0]} case(s) under 40.\n')
        out_file.write(f'{by_age_by_date[1]} case(s) 40 to 80.\n')
        out_file.write(f'{by_age_by_date[2]} case(s) over 80.\n')
        out_file.close()
        with open("output/diagnosed_data.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print(f'Sorry, but {chosen_file} was not found.\nThe program will now end.')
        exit()
    except IndexError as ie_error:
        print(ie_error)
        print(f'Sorry, but you tried to access information that does not exist.\nAre you sure you entered the correct'
              f' filename?\nThe program will now end.')
        exit()

main()