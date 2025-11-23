def student_discount(price):
    """
    Calculates student discount: 10% for price > 1000, 5% otherwise.
    """
    return price * (0.90 if price > 1000 else 0.95)

def regular_discount(price):
    """
    Calculates regular discount: 15% for price > 2000, no discount otherwise.
    """
    return price * (0.85 if price > 2000 else 1.00)

def discount(price, category):
    """
    Applies a discount based on the customer category.
    """
    if category == "student":
        return student_discount(price)
    return regular_discount(price)


# ---- INPUT FUNCTIONS ----

def main():
    """
    Main function to get user input and calculate the final discounted price.
    """
    try:
        price = float(input("Enter the price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    category = input("Enter category (student / regular): ").strip().lower()

    final_price = discount(price, category)
    print(f"Discounted price: {final_price}")

# Run the program
main()