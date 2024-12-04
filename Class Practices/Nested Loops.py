# Nested Loops Example 1: Colors and Shapes
colors = ["blue", "green", "yellow"]
shapes = ["circle", "square", "triangle"]

for color in colors:
    for shape in shapes:
        print(color, shape)

# Nested Loops Example 2: Multiplication Pairs
list1 = [2, 4, 6]
list2 = [1, 3, 5]

for a in list1:
    for b in list2:
        print(f"Multiplying {a} and {b} gives {a * b}")

# Nested Loops Example 3: Matrix Representation
rows = 2  # Representing 2 rows
columns = 3  # Representing 3 columns

for row in range(rows):  # Iterating over rows
    for col in range(columns):  # Iterating over columns
        print(f"Cell({row}, {col})")