'''

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

'''

# Days in Month Program with Leap Year Support
def is_leap_year(year):
    """
    Determine if a given year is a leap year.
    A leap year is divisible by 4, except for century years,
    which must be divisible by 400.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Dictionary mapping month numbers to days
month_days = {
    1: 31,   # January
    2: 28,   # February (default non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Month names for friendly output
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April", 
    5: "May", 6: "June", 7: "July", 8: "August", 
    9: "September", 10: "October", 11: "November", 12: "December"
}

# Program introduction
print("Find out how many days are in a month")

try:
    # Get month number from user
    month = int(input("Enter month number (1-12): "))
    
    # Check if month is valid
    if month not in month_days:
        print("Please enter a number between 1 and 12 only")
    else:
        # Special handling for February (leap year)
        if month == 2:
            # Ask for the year to determine leap year
            year = int(input("Enter the year: "))
            
            # Adjust February days based on leap year
            if is_leap_year(year):
                print(f"February {year} has 29 days")
            else:
                print(f"February {year} has 28 days")
        else:
            # For other months, simply print the days
            print(f"{month_names[month]} has {month_days[month]} days")

except ValueError:
    print("Invalid input. Please enter a valid number.")