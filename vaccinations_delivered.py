import csv

# individual list maker and wraps it into the dictionary
def dict_maker(filename):
    '''
    Creates a dictionary where each key is a week start day and the value is a list
    containing the values from the 5 corresponding columns of that date. It starts a list
    for each column, then at every date, it adds the current item from each of the 5 lists.
    :param filename: The name of the csv file that the user is making this dictionary with
    :return: The dictionary
    '''
    mega_dict = {}      # dictionary that will contain the dates and corresponding info
    week_start = []     # lists for 5 corresponding columns
    clinics = []
    congregate = []
    pharmacies = []
    primary = []
    other = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)                    # skip the row containing the headers
        for row in reader:
            week_start.append(row[0])   # add 'date' (1st column) to 1st list
            clinics.append(row[1])
            congregate.append(row[2])
            pharmacies.append(row[3])
            primary.append(row[4])
            other.append(row[5])        # add 'other' (6th column) to 6th list
    for i in range(len(week_start)):    # loop for how many weeks there are
        temp_list = [clinics[i], congregate[i], pharmacies[i], primary[i], other[i]]   # add current item of each list
        mega_dict[week_start[i]] = temp_list               # dictionary entry - Key: current date, Value: slot list
    return mega_dict

def vaccinations_by_date(date):
    """
    Adds up each source of vaccinations for a given date.
    :param date: each date in the dictionary, representing a week start
    :return: Total amount of vaccinations from all sources added up
    """
    int_list = []                   # empty list for integers to go
    for item in date:               # going through date list
        item = int(item)            # turn each item into an integer
        int_list.append(item)       # add it to the integer list
    total = sum(int_list)           # sum up the list of integers
    return total

def file_maker(full_dict):
    """
    Writes table showing each date and its corresponding amount of vaccinations delivered
    :param full_dict: Dictionary containing vaccinations amounts from each location
    """
    out_file = open("output/vaccine_doses_by_date.csv", "w")
    out_file.write(f'Date, Doses\n')
    for key in full_dict:                               # loops through dictionary
        doses = vaccinations_by_date(full_dict[key])    # function to find full amount of cases
        out_file.write(f'{key}, {doses}\n')              # writes each row with [date] and [case count]
    out_file.close()

def main():
    """
    Creates a csv table with dates and their corresponding vaccination delivery amounts from a file that a user chooses.
    """
    try:
        chosen_file = input('Which file would you like to analyze?\n')
        mega_dict = dict_maker(chosen_file)  # makes dictionary with dates as keys and corresponding lists as values
        file_maker(mega_dict)                     # takes dictionary
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
