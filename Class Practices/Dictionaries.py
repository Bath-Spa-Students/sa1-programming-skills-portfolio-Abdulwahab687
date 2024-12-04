# Creating an empty dictionary
my_dict = {}
print(my_dict)

# Verifying the type of an empty dictionary
my_dict = {}
print(my_dict, type(my_dict))

# Alternative way to initialize a dictionary
my_dict = dict()
print(my_dict, type(my_dict))

# Creating a dictionary with predefined key-value pairs
example_dict = {'color': 'red', 'fruit': 'apple', 'country': 'United Arab Emirates'}
print(example_dict)

# Adding key-value pairs to a dictionary
student_info = {
    'Name': 'Sheikh Abdul Wahab',
    'Roll Number': '7878',
    'Father\'s Name': 'Nasir Ali'
}
print(student_info, type(student_info))

# Accessing a specific value using a key
print(student_info["Name"], type(student_info))

# Demonstrating a key error if the key doesn't exist
try:
    print(student_info["Student"])  # Will throw a KeyError
except KeyError:
    print("KeyError: 'Student' not found in the dictionary.")

# Using the `get` method to safely retrieve a value
print(student_info.get("Student"))  # Returns None if the key is missing

# Providing a default value with `get` to handle missing keys
print(student_info.get("Student", "Bisma"))  # Returns "Anmol" as a default value

# Exploring the `.items()` method
print(student_info.items())  # Outputs a list of key-value pairs as tuples

# Accessing dictionary keys with the `.keys()` method
family_info = {
    'Name': 'Amna',
    'Roll Number': '1234',
    'Father\'s Name': 'Nasir Ali'
}
print(family_info.keys())