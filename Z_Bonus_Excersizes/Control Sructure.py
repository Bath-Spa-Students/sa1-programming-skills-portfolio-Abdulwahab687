
'''
Control Structures:
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
'''

# Prompt the user to input the alien's color
alien_color = input("Enter the alien's color (green, yellow, red): ").strip().lower()

# Determine points based on the alien's color
if alien_color == "green":
    print("Congratulations! You earned 5 points.")
elif alien_color == "yellow":
    print("Great job! You earned 10 points.")
elif alien_color == "red":
    print("Amazing! You earned 15 points.")
else:
    print("Oops! That doesn't seem like a valid alien color. No points awarded.")
