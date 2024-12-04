# Ask the player to specify the alien's color
alien_color = input("Enter the alien's color (green, orange, yellow): ").strip().lower()

# Check if the alien's color is green and award points
if alien_color == "green":
    print("Awesome! You earned 5 points for spotting a green alien.")