'''

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

'''

# Define the correct password
CORRECT_PASSWORD = "abbas"

# Set the maximum number of allowed attempts
MAX_ATTEMPTS = 5

# Initialize the attempt counter
attempts = 0

# Start authentication loop
while attempts < MAX_ATTEMPTS:
    # Prompt user for password and remove whitespace
    user_password = input("Please enter the password: ").strip()
    
    # Mask the password for security display
    masked_password = '*' * len(user_password)
    
    # Increment attempt counter
    attempts += 1
    
    # Validate password
    if user_password == CORRECT_PASSWORD:
        print("Access granted. Welcome User!")
        break
    else:
        # Calculate remaining attempts
        remaining_attempts = MAX_ATTEMPTS - attempts
        
        # Display incorrect password feedback
        print(f"Incorrect password: {masked_password}")
        print(f"You have {remaining_attempts} attempt(s) remaining.")
        
        # Provide strategic hint on last attempt
        if attempts == MAX_ATTEMPTS - 1:
            print("Hint: The password is a name.")
        
        # Lock out after maximum attempts
        if attempts == MAX_ATTEMPTS:
            print("Access denied. You have been locked out.")
            print("Maximum attempts reached. Authorities have been alerted.")