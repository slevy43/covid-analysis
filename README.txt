This is a 3-part program, that takes CSV information from the London/Middlesex Health Unit related to COVID-19 case data or vaccination delivery data, and outputs an file with analytical insights

covid_diagnosed.py
  - Purpose: Creates output text file containing detailed insights into location and age breakdown of cases, as well as breaking down the highest-case day in the data set.
  
    - INPUT: input/covid.csv
    - OUTPUT: output/diagnosed_data.txt

vaccination_analysis.py
- Purpose: Creates output text file detailing the amount, median, and highest/lowest ranking weeks of vaccinations delivered
    - INPUT: input/vaccines.csv
    - OUTPUT: output/vaccination_data.txt

vaccinations_delivered.py
- Purpose: Creates CSV file with the amount of doses delivered per day, from CSV containing itemized chart of vaccines delivered during a given period
    - INPUT: input/vaccines.csv
    - OUTPUT: output/vaccine_doses_by_date.csv
