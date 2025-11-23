def find_common():
    """
    Prompts the user for two lists of numbers, finds the common
    elements, and returns them as a new list. Handles invalid input.
    """
    a_input = input("Enter numbers for list A (comma-separated): ")
    b_input = input("Enter numbers for list B (comma-separated): ")

    # Convert to integer lists
    try:
        a = [int(x) for x in a_input.split(",")]
        b = [int(x) for x in b_input.split(",")]
    except ValueError:
        print("Error: Please enter only numbers separated by commas.")
        return []

    # Find common values
    common = [num for num in a if num in b]

    return common


# --- Main execution ---
result = find_common()
print("Common elements:", result)
