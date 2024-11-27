'''

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.

'''

def search_names():
    """
    Interactive name search program with enhanced functionality.
    Allows users to search for names in a predefined list.
    """
    # Predefined list of names
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    # Program introduction
    print("Welcome to the Name Search Assistant!")
    print("Our current list of names:", names)
    
    while True:
        # User input for name search
        find = input("\nWhat name are you looking for? (or 'quit' to exit): ").strip()
        
        # Exit condition
        if find.lower() == 'quit':
            print("Thank you for using the Name Search Assistant. Goodbye!")
            break
        
        # Search functionality with multiple output options
        if find in names:
            # Find index for additional information
            index = names.index(find)
            print(f"✅ Yes, '{find}' is available in the list!")
            print(f"   Position: {index + 1} in the list")
        else:
            print(f" Sorry, '{find}' is not in the list.")
            
            # Suggest similar names (case-insensitive)
            similar_names = [name for name in names if name.lower().startswith(find.lower())]
            if similar_names:
                print("   Suggestions:", ', '.join(similar_names))

# Run the search program
if __name__ == "__main__":
    search_names()