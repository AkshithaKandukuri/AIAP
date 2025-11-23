# BankAccount class demonstration.

class BankAccount:
    """A simple bank account class with deposit, withdrawal, and balance methods."""

    def __init__(self, owner, initial_balance=0):
        """Initialize account with owner and optional initial balance."""
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn.")

    def get_balance(self):
        """Return the current account balance."""
        return self.balance

# Main program with user input
if __name__ == "__main__":
    # Get account owner name
    owner_name = input("Enter account owner name: ")
    
    # Get initial balance (optional)
    initial_balance_input = input("Enter initial balance (default 0): ").strip()
    if initial_balance_input:
        try:
            initial_balance = float(initial_balance_input)
        except ValueError:
            print("Invalid input. Using default balance of 0.")
            initial_balance = 0
    else:
        initial_balance = 0
    
    # Create bank account
    account = BankAccount(owner_name, initial_balance)
    print(f"\nAccount created for {owner_name} with initial balance: ${initial_balance:.2f}\n")
    
    # Interactive menu
    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            amount_input = input("Enter amount to deposit: ")
            try:
                amount = float(amount_input)
                account.deposit(amount)
                print(f"Current Balance: ${account.get_balance():.2f}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "2":
            amount_input = input("Enter amount to withdraw: ")
            try:
                amount = float(amount_input)
                account.withdraw(amount)
                print(f"Current Balance: ${account.get_balance():.2f}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "3":
            print(f"Current Balance: ${account.get_balance():.2f}")
        
        elif choice == "4":
            print("Thank you for using Bank Account system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")