import csv

# ANALYZER
def tuple_maker(filename):
    """
    Creates the list of tuples. Format of each tuple is [date], [vax amount]
    :param filename: The file that the user has chosen
    :return: List of tuples containing [date], [vax amount]
    """
    tuple_list = []                        # start empty list for tuples
    with open(filename, 'r') as csv_file:  # open file for reading
        reader = csv.reader(csv_file)
        next(reader)                       # skip the row containing the headers
        for row in reader:                 # for each row in the file
            row_tuple = row[0], row[1]     # make a tuple from the date and vax amount
            tuple_list.append(row_tuple)   # add this tuple to the tuple list
    return tuple_list

def fewest_vaccinations(tuple_list):
    """
    Finds the three highest vax amounts. Puts the values into a list and assigns the first, second and third items
    in the list to the corresponding variables.
    :param tuple_list: List of tuples containing pairs of dates and corresponding case counts
    :return: A tuple containing the first, second, and third-lowest case counts
    """
    pair_dict = dict(tuple_list)                        # dictionary - keys: dates, vals: vax count
    sorted_vax = []
    for value in pair_dict.values():                    # iterate through the vax counts from the dictionary
        value = int(value)
        sorted_vax.append(value)                        # make it an integer and add it to a list
    sorted_vax.sort()                                   # sort the list from lowest to highest
    first_few = ('date', '0')
    second_few = ('date', '0')                            # placeholder values in case of crash
    third_few = ('date', '0')
    for key in pair_dict:                               # iterate through each date in the dict
        pair_dict[key] = pair_dict[key].strip()
        if pair_dict[key] == str(sorted_vax[0]):        # if the date's value equals the lowest vax count
            first_few = (key, pair_dict.get(key))       # store that date and value as a tuple under first_few
        elif pair_dict[key].strip() == str(sorted_vax[1]):
            second_few = (key, pair_dict.get(key))
        elif pair_dict[key].strip() == str(sorted_vax[2]):
            third_few = (key, pair_dict.get(key))
    fewest_tuple = (first_few, second_few, third_few,)  # make tuple out of lowest, middle, and highest pairs
    return fewest_tuple

def most_vaccinations(tuple_list):
    """
    Finds the three highest vax amounts. Puts the values into a list and assigns the first, second and third items
    in the list to the corresponding variables.
    :param tuple_list: List of tuples containing [date], [vax amount]
    :return: A tuple containing the first, second, and third highest case counts
    """
    pair_dict = dict(tuple_list)                        # dictionary - keys: dates, vals: vax count
    sorted_vax = []
    for value in pair_dict.values():                    # iterate through the vax counts from the dictionary
        value = int(value)
        sorted_vax.append(value)                        # make it an integer and add it to a list
    sorted_vax.sort()                                   # sort the list from lowest to highest
    first_most = ('date', '0')
    second_most = ('date', '0')                           # placeholder values in case of crash
    third_most = ('date', '0')
    for key in pair_dict:                               # iterate through each date in the dict
        pair_dict[key] = pair_dict[key].strip()
        if pair_dict[key] == str(sorted_vax[-1]):       # if the date's value equals the lowest vax count
            first_most = (key, pair_dict.get(key))      # store that date and value as a tuple under first_few
        elif pair_dict[key] == str(sorted_vax[-2]):
            second_most = (key, pair_dict.get(key))
        elif pair_dict[key] == str(sorted_vax[-3]):
            third_most = (key, pair_dict.get(key))
    most_tuple = (first_most, second_most, third_most,)  # make tuple out of lowest, middle, and highest pairs
    return most_tuple

def median_number_vaccinations(tuple_list):
    """
    Finds the median number of vaccinations from the data. Either rounds down to find the middle number or
    averages the two middle numbers depending on if the list has an odd or even amount of items.
    :param tuple_list: List of tuples containing [date], [vax amount]
    :return: Median vax amount value from data as a float
    """
    vax_list = []                                        # empty list for all vax values
    for pair in tuple_list:                              # for every pair of [date], [vax amount]
        vax_list.append(int(pair[1]))                    # add each vax value to empty list
    vax_list.sort()                                      # sort vax list from lowest to highest amount
    if len(vax_list) % 2 != 0:                           # if the length of the list is not divisible by 2
        median_index = int(len(vax_list)/2 - 0.5)        # round down to find the middle number
        median = float(vax_list[median_index])           # median is a float of the middle number of the list
    else:
        median_index_lower = int(len(vax_list)/2 - 0.5)        # list length / 2 and round down
        median_index_higher = int(len(vax_list)/2 + 0.5)       # list length / 2 and round up
        lower_value = int(vax_list[median_index_lower])        # finding value of lower middle index
        higher_value = int(vax_list[median_index_higher])      # finding value of higher middle index
        median = (lower_value + higher_value) / 2.0            # finding average of two values
    return median


def vaccination_total(tuple_list):
    """
    Finds the total amount of vaccinations. Increments the vax amount from each tuple to a counter.
    :param tuple_list: List of tuples containing [date], [vax amount]
    :return: Integer value of total vaccinations
    """
    vax_total = 0                    # start counter
    for pair in tuple_list:          # each pair containing [date], [vax amount]
        vax_total += int(pair[1])    # get number from vax amount and add it to the counter
    return vax_total

def file_maker(few_vax, most_vax, median, total):
    """
    Stores formatted lines to a file, then loops through the file to display its contents
    """
    out_file = open("output/vaccination_data.txt", "w")
# TOTAL
    out_file.write(f'Total number of vaccinations: {total}\n')
# MEDIAN
    out_file.write(f"Median number of vaccinations: {format(median, '.2f')}\n")
# FEW VAX
    out_file.write(f'The week of {few_vax[0][0]} saw the fewest vaccinations: {few_vax[0][1]}\n')
    out_file.write(f'The week of {few_vax[1][0]} saw the second fewest vaccinations: {few_vax[1][1]}\n')
    out_file.write(f'The week of {few_vax[2][0]} saw the third fewest vaccinations: {few_vax[2][1]}\n')
# MOST VAX
    out_file.write(f'The week of {most_vax[0][0]} saw the most vaccinations: {most_vax[0][1]}\n')
    out_file.write(f'The week of {most_vax[1][0]} saw the second most vaccinations: {most_vax[1][1]}\n')
    out_file.write(f'The week of {most_vax[2][0]} saw the third most vaccinations: {most_vax[2][1]}\n')
    out_file.close()
    with open("output/vaccination_data.txt", "r") as file:  # open up the new file for reading
        for line in file:
            print(line.strip())                      # print each line in the file

def main():
    """
     Stores and displays formatted values from file containing dates and their corresponding vaccination amounts.
     Shows weeks with the top 3 and bottom 3 case counts, the total and median case counts.
    """
    try:
        chosen_file = input('Which file would you like to analyze?\n')
        tuple_list = tuple_maker(chosen_file)                 # make list containing tuples: [date], [vax amount]
        few_vax = fewest_vaccinations(tuple_list)             # store tuple of (first, second, third) fewest counts
        most_vax = most_vaccinations(tuple_list)              # store tuple of (first, second, third) highest counts
        median = median_number_vaccinations(tuple_list)       # store value of median vax amount
        total = vaccination_total(tuple_list)                 # store value of total vaccinations
        file_maker(few_vax, most_vax, median, total)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print(f"Sorry, but {chosen_file} was not found.\nThe program will now end.")
        exit()

main()
