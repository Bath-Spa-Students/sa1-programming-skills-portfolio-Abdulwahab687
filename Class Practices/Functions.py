# Function with no return value (void function)
def greet_users():
    print("Hello, everyone!")

# Invoking the function
greet_users()

# Using a local variable inside a function
def display_message():
    greeting = "Hello, everyone!"  # Local variable
    print(greeting)

# Calling the function
display_message()

# Functions with the same local variable name but different contexts
def say_hi():
    text = "Hi there!"  # Local variable
    print(text)

def say_hello():
    text = "Hello, world!"  # Local variable
    print(text)

# Invoking the functions
say_hi()
say_hello()