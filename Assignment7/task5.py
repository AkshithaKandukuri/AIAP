numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError:
    print("Invalid index! Please select a valid position.")