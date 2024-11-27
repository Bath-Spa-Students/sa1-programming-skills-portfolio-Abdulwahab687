'''

Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:
Instructions:

The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.

'''

def check_even_odd(number):
    """
    Determine if a given number is even or odd.
    
    Args:
        number (int): The number to be checked
    
    Returns:
        str: A message indicating whether the number is even or odd
    """
    try:
        # Check if the number is even (divisible by 2 with no remainder)
        if number % 2 == 0:
            return f"{number} is an even number."
        else:
            return f"{number} is an odd number."
    except TypeError:
        return "Invalid input. Please enter a valid integer."

def main():
    """
    Main function to get user input and check if the number is even or odd.
    Handles input and displays the result.
    """
    try:
        # Prompt user to enter a number
        num = int(input("Enter a number to check if it's even or odd: "))
        
        # Call the check_even_odd function and print the result
        result = check_even_odd(num)
        print(result)
    
    except ValueError:
        print("Error: Please enter a valid integer.")

# Ensure the script runs only when directly executed
if __name__ == "__main__":
    main()