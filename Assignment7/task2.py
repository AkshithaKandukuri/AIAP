n = int(input("Enter value for n: "))
def count_down(n):
    while n >= 0:
        print(n)
        n -= 1  # Decrement n by 1 each loop
print(count_down(n))