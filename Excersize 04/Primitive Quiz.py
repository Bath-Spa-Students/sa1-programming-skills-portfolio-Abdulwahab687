## Exercise 4: Primitive Quiz - 30 Marks

# Dictionary to store country-capital pairs
# Using dictionary for easy expansion and maintenance of quiz questions
QUIZ_DATA = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'United Kingdom': 'London',
    'Portugal': 'Lisbon',
    'Netherlands': 'Amsterdam',
    'Greece': 'Athens',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo'
}

def check_answer(user_answer, correct_answer):
    """
    Validates user's answer against correct answer, ignoring case
    Args:
        user_answer (str): The answer provided by user
        correct_answer (str): The correct answer to compare against
    Returns:
        bool: True if answer is correct, False otherwise
    """
    return user_answer.lower().strip() == correct_answer.lower()

def run_quiz():
    """
    Main function to conduct the European capitals quiz
    Tracks score and provides feedback for each answer
    """
    # Initialize score counter
    score = 0
    total_questions = len(QUIZ_DATA)
    
    print("\n=== European Capitals Quiz ===")
    print(f"Answer {total_questions} questions about European capitals!\n")
    
    try:
        # Iterate through each country-capital pair
        for country, capital in QUIZ_DATA.items():
            # Get user's answer with proper formatting
            user_answer = input(f"What is the capital of {country}? ")
            
            # Check answer and provide immediate feedback
            if check_answer(user_answer, capital):
                print("✓ Correct! Well done!\n")
                score += 1
            else:
                print(f"✗ Wrong! The capital of {country} is {capital}.\n")
        
        # Calculate and display final score
        percentage = (score / total_questions) * 100
        print("=== Quiz Complete ===")
        print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")
        
        # Provide performance feedback
        if percentage == 100:
            print("Perfect score! Excellent knowledge!")
        elif percentage >= 70:
            print("Good job! You know your European capitals well!")
        else:
            print("Keep learning! Practice makes perfect!")
            
    except KeyboardInterrupt:
        print("\nQuiz interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

# Simple version (basic requirements only)
def simple_quiz():
    """
    Basic version of the quiz with single question
    Demonstrates core functionality without complexity
    """
    try:
        # Get answer for single question
        answer = input("What is the capital of France? ")
        
        # Check answer ignoring case
        if check_answer(answer, "Paris"):
            print("Correct! Well done!")
        else:
            print("Wrong! The capital of France is Paris.")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the appropriate version based on requirements
if __name__ == "__main__":
    # Comment/uncomment the version you want to run
    run_quiz()          # Advanced version
    # simple_quiz()     # Basic version
