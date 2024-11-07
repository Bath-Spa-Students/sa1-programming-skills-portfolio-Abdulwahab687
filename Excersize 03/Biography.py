## Exercise 3: Biography - 25 Marks

# Solution addressing both basic and advanced requirements with error handling

def get_valid_age():
    """
    Helper function to validate age input.
    Keeps asking until a valid integer age is provided.
    Returns: int - validated age
    """
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 150:  # Basic age range validation
                return age
            else:
                print("Please enter a realistic age (0-150)")
        except ValueError:
            print("Please enter a valid number for age")

def create_biography():
    """
    Main function to collect and display user biography information.
    Handles multi-word inputs and validates data before storing.
    """
    # Initialize empty dictionary to store biographical information
    bio_data = {}
    
    # Collect user information with proper error handling
    try:
        # Get full name (handles multiple words)
        bio_data['name'] = input("Enter your full name: ").strip()
        
        # Get hometown (handles multiple words)
        bio_data['hometown'] = input("Enter your hometown: ").strip()
        
        # Get age with validation
        bio_data['age'] = get_valid_age()
        
        # Display biography using formatted string
        print("\n=== Your Biography ===")
        print(f"""Name: {bio_data['name']}
Hometown: {bio_data['hometown']}
Age: {bio_data['age']} years old""")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    create_biography()
