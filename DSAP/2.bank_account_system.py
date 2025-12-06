class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Account Holder: {self.name}")
        print(f"Available Balance: ₹{self.balance}")


# Main Program
acc_no = input("Enter Account Number: ")
name = input("Enter Account Holder Name: ")
account = BankAccount(acc_no, name)

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid Choice! Try again.")
