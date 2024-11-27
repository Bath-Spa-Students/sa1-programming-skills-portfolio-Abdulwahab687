'''

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

'''

# Capital Cities Quiz
print("Welcome to the Capital Cities Quiz!")
print("Try your best to answer the following questions.\n")

# Initialize score
score = 0
total_questions = 10

# Question 1
ans = input("Question 1: What is the capital of France? ")
if ans.lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.\n")

# Question 2
ans = input("Question 2: What is the capital of Germany? ")
if ans.lower() == "berlin":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Berlin.\n")

# Question 3
ans = input("Question 3: What is the capital of Italy? ")
if ans.lower() == "rome":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Rome.\n")

# Question 4
ans = input("Question 4: What is the capital of Spain? ")
if ans.lower() == "madrid":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Madrid.\n")

# Question 5
ans = input("Question 5: What is the capital of Portugal? ")
if ans.lower() == "lisbon":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Lisbon.\n")

# Question 6
ans = input("Question 6: What is the capital of the United Kingdom? ")
if ans.lower() == "london":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is London.\n")

# Question 7
ans = input("Question 7: What is the capital of Ireland? ")
if ans.lower() == "dublin":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Dublin.\n")

# Question 8
ans = input("Question 8: What is the capital of Sweden? ")
if ans.lower() == "stockholm":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Stockholm.\n")

# Question 9
ans = input("Question 9: What is the capital of Greece? ")
if ans.lower() == "athens":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Athens.\n")

# Question 10
ans = input("Question 10: What is the capital of the Netherlands? ")
if ans.lower() == "amsterdam":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Amsterdam.\n")

# Quiz finished
print("Quiz completed!")
print(f"You got {score} out of {total_questions} questions correct.")
print("Thanks for playing!")