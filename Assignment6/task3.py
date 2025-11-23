age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")