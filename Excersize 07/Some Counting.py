'''

Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case. 

* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
* You may include all loops in a single project

'''
# Comprehensive Number Counting Exercises

def print_section_header(description):
    """Helper function to print section headers for readability"""
    print(f"\n--- {description} ---")

def count_exercises():
    """Execute all counting exercises"""
    # Exercise 1: Count up from 0 to 50 in increments of 1
    print_section_header("Counting up from 0 to 50")
    for number in range(0, 51):
        print(number)

    # Exercise 2: Count down from 50 to 0 in decrements of 1
    print_section_header("Counting down from 50 to 0")
    for number in range(50, -1, -1):
        print(number)

    # Exercise 3: Count up from 30 to 50 in increments of 1
    print_section_header("Counting from 30 to 50")
    for number in range(30, 51):
        print(number)

    # Exercise 4: Count down from 50 to 10 in decrements of 2
    print_section_header("Counting down 50 to 10 by 2s")
    for number in range(50, 9, -2):
        print(number)

    # Exercise 5: Count up from 100 to 200 in increments of 5
    print_section_header("Count up from 100 to 200 by 5s")
    for number in range(100, 201, 5):
        print(number)

# Run the counting exercises
if __name__ == "__main__":
    count_exercises()
