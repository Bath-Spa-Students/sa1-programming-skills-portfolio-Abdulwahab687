'''

## Exercise 9: Hello - 10 Marks

Fill in the blanks in the code below so that the function hello() prints "Hello" to the console.


def hello():
    ____  # Fill in this blank to print "Hello" to the console

def main():
    ____  # Fill in this blank to call the hello() function

if __name__ == "__main__":
    main()

'''

def hello():
    """
    Print a greeting message to the console.
    
    This function demonstrates a simple print statement.
    """
    print("Hello")

def main():
    """
    Main function to call the hello() function.
    
    Serves as the entry point for the program's execution.
    """
    hello()  # Call the hello function to display the greeting

# Ensure the script runs only when directly executed
if __name__ == "__main__":
    main()