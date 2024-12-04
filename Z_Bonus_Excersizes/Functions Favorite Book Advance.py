
'''
Write a function called favorite_book() that accepts one parameter, title. The function
should print a message, such as One of my
'''

# Creating a function to display a favorite book
def show_favorite_book(book_title):
    print(f"A favorite book of mine is {book_title}.")

# Prompting the user to input their favorite book
favorite_title = input("What is your favorite book? ")

# Calling the function with the user's input
show_favorite_book(favorite_title)
