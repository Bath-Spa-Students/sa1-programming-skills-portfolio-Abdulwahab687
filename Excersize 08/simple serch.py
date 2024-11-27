'''

## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names
 ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.

'''
def search_names(name_list, target_name):
    """
    Search for a specific name in a list of names.
    
    Args:
        name_list (list): List of names to search through
        target_name (str): Name to find in the list
    
    Returns:
        tuple: (found status, index of name if found)
    """
    print(f"The list of names: {name_list}")
    
    # Search for the name using different methods
    if target_name in name_list:
        # Find the index of the name
        index = name_list.index(target_name)
        print(f"Found {target_name}! Position: {index + 1}")
        return True, index
    else:
        print(f"Can't find {target_name} in the list")
        return False, -1

# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Perform the search
search_names(names, "Sam")

# Optional: Additional search demonstrations
def advanced_search_demo():
    """Demonstrate additional search capabilities"""
    print("\n--- Advanced Search Demonstration ---")
    
    # Search for multiple names
    search_names(names, "Dave")
    search_names(names, "Mike")  # A name not in the list
    
    # Case-sensitive search
    print("\nCase-Sensitive Search:")
    if "sam" in names:
        print("Found 'sam'")
    else:
        print("'sam' not found (case-sensitive)")

# Run the advanced demo
advanced_search_demo()