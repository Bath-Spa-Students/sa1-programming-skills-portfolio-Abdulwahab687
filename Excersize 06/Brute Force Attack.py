'''

## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

'''
# Define the correct password as a constant
CORRECT_PASSWORD = "12345"

# Track number of attempts
attempts = 0
max_attempts = 3

# Start a loop that continues until the correct password is entered
while attempts < max_attempts:
    # Prompt the user to enter a password
    entered_password = input("Please enter the password: ")
    
    # Increment attempts counter
    attempts += 1
    
    # Check if the entered password matches the correct one
    if entered_password == CORRECT_PASSWORD:
        # If correct, display a success message and exit the loop
        print("Permission to enter granted. Good day!")
        break  # Exit the loop
    else:
        # Calculate remaining attempts
        remaining_attempts = max_attempts - attempts
        
        # If attempts are exhausted
        if remaining_attempts == 0:
            print("Too many incorrect attempts. Access denied.")
        else:
            # If incorrect, let the user know and how many attempts are left
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
