
# Assume that the current date is 2022-12-19. Write a program that will request the user's date of birth and calculate their age in hours. The program must validate that the entered date is in the correct date format (yyyy-mm-dd). The program must also validate that the date of birth is not in the future(again assume a current date of 2022-12-19) nor way too much in the past than that of the oldest person alive (assume this is Lucile Randon born in 1904-02-11). Only when the date of birth entered meets all of these criteria should the age in days be printed.

# Ex: If the input of the program is:

# 1976-10-28

# the output of the program is:

# 16853 days.

# Ex: If the input of the program is:

# 2098-01-01

# the output of the program is:

# Incorrect date, your birthday cannot be in the future!

# Ex: If the input of the program is:

# 1900-01-01

# the output of the program is:

# Incorrect date, you cannot be older than Lucile Randon!

# Ex: If the input of the program is: 1900/01/01

# the output of the program is:

# Incorrect date format, please try again!

from datetime import datetime

def calculate_age_in_hours(birth_str, current_date_str):
    current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
    try:
        birth_date = datetime.strptime(birth_str, '%Y-%m-%d')
    except Exception:
        return "Incorrect date format, please try again!"
    oldest_person = datetime(1904, 2, 11)
    if birth_date < oldest_person:
        return "Incorrect date, you cannot be older than Lucile Randon!"
    elif birth_date > current_date:
        return "Incorrect date, your birthday cannot be in the future!"
    else:
        age_in_hours = (current_date - birth_date).days * 24
        return f"{age_in_hours} hours."
        
if __name__ == '__main__':
    current_date_str = '2022-12-19'
    birth_str = input()
    print(calculate_age_in_hours(birth_str, current_date_str))