from typing import List, Union
from numbers import Number

def find_largest(numbers: List[Union[int, float]]) -> Union[int, float]:
    if not numbers:
        raise ValueError("Cannot find largest number in an empty list")
    
    if not all(isinstance(x, Number) for x in numbers):
        raise TypeError("List must contain only numbers")
    
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    test_lists = [
        [1, 5, 3, 9, 2, 6],
        [10.5, -3, 8.1, 15.7, 0],
        [-10, -20, -5, -15],
        [42]
    ]
    
    print("Testing with different lists:")
    print("-" * 40)
    
    for test_list in test_lists:
        print(f"List: {test_list}")
        print(f"Largest number: {find_largest(test_list)}")
        print(f"Verification using max(): {max(test_list)}")
        print("-" * 40)
    
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.split()]
        result = find_largest(numbers)
        print(f"\nThe largest number in your list is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")