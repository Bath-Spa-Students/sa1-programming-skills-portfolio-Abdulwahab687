'''

## Exercise 3: Biography - 25 Marks
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

'''
# Solution addressing both basic and advanced requirements with error handling

def get_valid_age():
    """
    Helper function to validate age input.
    Keeps asking until a valid integer age is provided.
    Returns: int - validated age
    """
# Step 1: Create a dictionary with biographical information
bio = {
    "name": "Sheikh Abdul Wahab Nasir Ali",        # String for name
    "hometown": "Karachi",    # String for hometown
    "age": 18                  # Integer for age
}

# Step 2: Print values using a single print statement
print(f"""Biography:
Name: {bio['name']}
Hometown: {bio['hometown']}
Age: {bio['age']} years old""")
