
'''
Loops- Pizza Toppings :
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
'''

# Continuously ask for pizza toppings until the user decides to stop
active = True
while active:
    selected_topping = input("What topping would you like on your pizza? (Type 'quit' to finish): ")

    # Check if the user wants to quit
    if selected_topping.lower() == 'quit':
        print("Pizza topping selection has ended.")
        active = False
    else:
        # Confirm the addition of the topping
        print(f"{selected_topping} will be added to your pizza!")