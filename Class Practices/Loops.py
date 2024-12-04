# Iterating through a list of fruits
fruit_list = ["apple", "banana", "cherry"]
for fruit in fruit_list:
    print(fruit)

# Iterating through a list of car models
car_models = ["ls430", "ls460", "lx570"]
for car in car_models:
    print(car)

# The break statement: Exiting the loop when a condition is met
car_models = ["ls430", "ls460", "lx570"]
for car in car_models:
    print(car)
    if car == "ls460":
        break

# Using the range function to generate a sequence of numbers
for number in range(8):
    print(number)

# Generating a sequence with a step increment of 3
for number in range(2, 30, 3):
    print(number)

# While loop example: Executing as long as a condition is true
# Print values of 'i' while it remains less than 10
counter = 1
while counter < 10:
    print(counter)
    counter += 1  # Increment counter by 1

# Another while loop example with a fixed count
current_count = 1
while current_count <= 5:
    print("Current Count:", current_count)
    current_count += 1