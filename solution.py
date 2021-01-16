#created by : Yassine

# defining leap and ordinary years on a dictionary using this format :
# <month> : [total days : last month's total days + the month that was before it]
months_of_leap_year = {
    'january': [31, 0],
    'february': [29, 31],
    'march': [31, 60],
    'april': [30, 91],
    'may': [31, 121],
    'june': [30, 152],
    'july': [31, 182],
    'august': [31, 213],
    'september': [30, 244],
    'october': [31, 274],
    'november': [30, 305],
    'december': [31, 335]
}
months_of_ordinary_year = {
    'january': [31, 0],
    'february': [28, 31],
    'march': [31, 59],
    'april': [30, 90],
    'may': [31, 120],
    'june': [30, 151],
    'july': [31, 181],
    'august': [31, 212],
    'september': [30, 243],
    'october': [31, 273],
    'november': [30, 304],
    'december': [31, 334]
}

# creating the main function
def age_calculator(birthday, birthmonth, birthyear, current_day, current_month, current_year):
    number_of_leap_years = 0
    for x in range(birthyear, current_year): #using a for loop we determine the number of leap years between the birthyear and the current year
        if x % 4 == 0:
            number_of_leap_years += 1
    age_in_years = int(current_year) - int(birthyear)
    number_of_ordinary_years = age_in_years - number_of_leap_years
    age_in_days = (number_of_ordinary_years * 365) + (number_of_leap_years * 366)

    # getting the number of days from 01/01/birthyear till birthday/birthmonth/birthyear
    if birthyear % 4 == 0:
        days_in_birthyear = (months_of_leap_year[str(birthmonth.lower())][-1] + birthday)
    else:
        days_in_birthyear = (months_of_ordinary_year[str(birthmonth.lower())][-1] + birthday)


    # getting the number of days from 01/01/current_year till current_day/current_month/current_year
    if current_year % 4 == 0:
        days_in_currentyear = months_of_leap_year[current_month.lower()][-1] + current_day
    else:
        days_in_currentyear = months_of_ordinary_year[current_month.lower()][-1] + current_day

    age_in_days += (days_in_currentyear - days_in_birthyear)
    print(f'Age : {age_in_days} day (excluding today)\n ')
# Test case :
age_calculator(25, 'january', 2000, 28, 'march', 2020) #1

# You'll get an error if the month is not typed correctly or if the day = 01,02..
# Also if the day number above 31 the results won't be correct


