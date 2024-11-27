'''

## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

'''

# Dictionary mapping month numbers to days
month_days = {
    1: 31,   # January
    2: 28,   # February (standard non-leap year)
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

# Program introduction
print("Find out how many days are in a month")

try:
    # Get month number from user
    month = int(input("Enter month number (1-12): "))
    
    # Check if month is valid and print days
    if month in month_days:
        days = month_days[month]
        month_names = {
            1: "January", 2: "February", 3: "March", 4: "April", 
            5: "May", 6: "June", 7: "July", 8: "August", 
            9: "September", 10: "October", 11: "November", 12: "December"
        }
        print(f"{month_names[month]} has {days} days")
    else:
        print("Please enter a number between 1 and 12 only")

except ValueError:
    print("Invalid input. Please enter a valid number.")