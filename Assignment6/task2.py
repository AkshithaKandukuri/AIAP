#! /usr/bin/env python3

# Class with constructor and display_details() method
class Product:
	def __init__(self, name, category, price):
		self.name = name
		self.category = category
		self.price = price

	def display_details(self):
		print(f"Product: {self.name}")
		print(f"Category: {self.category}")
		print(f"Price: ${self.price:.2f}")


def print_multiples(number):
	"""Prints the first 10 multiples of a given number using a loop."""
	for i in range(1, 11):
		multiple = number * i
		print(f"{number} x {i} = {multiple}")


def main():
	name = input("Enter product name: ").strip() or "Sample Item"
	category = input("Enter product category: ").strip() or "General"
	price_str = input("Enter product price: ").strip() or "0"
	try:
		price = float(price_str)
	except ValueError:
		price = 0.0

	item = Product(name, category, price)
	item.display_details()


if __name__ == "__main__":
	main()
