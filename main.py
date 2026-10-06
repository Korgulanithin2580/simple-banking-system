from repositories.account_repository import AccountRepository
from services.account_service import AccountService
from services.auth_service import AuthService
from services.transaction_service import TransactionService


# ==========================================
# INITIALIZATION
# ==========================================

DATA_FILE = "data/accounts.json"

repository = AccountRepository(DATA_FILE)

account_service = AccountService(repository)
auth_service = AuthService(repository)
transaction_service = TransactionService(repository)


# ==========================================
# CREATE ACCOUNT
# ==========================================

def create_account_menu():

    print("\n================================")
    print("        CREATE ACCOUNT")
    print("================================")

    name = input("Enter your name: ")
    password = input("Create password: ")

    try:

        account_number = account_service.create_account(
            name,
            password
        )

        print("\nAccount created successfully!")
        print("Your Account Number:", account_number)
        print("Please remember your account number.")

    except ValueError as error:

        print("\nError:", error)


# ==========================================
# LOGIN
# ==========================================

def login_menu():

    print("\n================================")
    print("             LOGIN")
    print("================================")

    account_number = input("Enter account number: ")
    password = input("Enter password: ")

    try:

        logged_in_account = auth_service.login(
            account_number,
            password
        )

        print("\nLogin successful!")
        print("Welcome to the Banking System.")

        user_menu(logged_in_account)

    except ValueError as error:

        print("\nLogin failed:", error)


# ==========================================
# ADD MONEY
# ==========================================

def add_money_menu(account_number):

    print("\n================================")
    print("           ADD MONEY")
    print("================================")

    try:

        amount = float(
            input("Enter amount to add: ₹")
        )

        transaction_service.add_money(
            account_number,
            amount
        )

        print("\nMoney added successfully!")
        print(f"Amount added: ₹{amount:.2f}")

        balance = transaction_service.check_balance(
            account_number
        )

        print(f"New Balance: ₹{balance:.2f}")

    except ValueError as error:

        print("\nFailed:", error)


# ==========================================
# CHECK BALANCE
# ==========================================

def check_balance_menu(account_number):

    print("\n================================")
    print("         CHECK BALANCE")
    print("================================")

    try:

        balance = transaction_service.check_balance(
            account_number
        )

        print(f"\nAccount Number : {account_number}")
        print(f"Current Balance: ₹{balance:.2f}")

    except ValueError as error:

        print("\nError:", error)


# ==========================================
# TRANSFER MONEY
# ==========================================

def transfer_money_menu(account_number):

    print("\n================================")
    print("         TRANSFER MONEY")
    print("================================")

    receiver_account = input(
        "Enter receiver account number: "
    )

    try:

        amount = float(
            input("Enter amount to transfer: ₹")
        )

        transaction_service.transfer(
            account_number,
            receiver_account,
            amount
        )

        print("\nTransfer successful!")
        print(f"Amount transferred: ₹{amount:.2f}")
        print(f"To account: {receiver_account}")

        balance = transaction_service.check_balance(
            account_number
        )

        print(f"Remaining Balance: ₹{balance:.2f}")

    except ValueError as error:

        print("\nTransfer failed:", error)


# ==========================================
# TRANSACTION HISTORY
# ==========================================

def transaction_history_menu(account_number):

    print("\n================================")
    print("      TRANSACTION HISTORY")
    print("================================")

    try:

        transactions = transaction_service.transaction_history(
            account_number
        )

        if not transactions:

            print("\nNo transactions found.")

        else:

            for number, transaction in enumerate(
                transactions,
                start=1
            ):

                print("\n--------------------------------")
                print(f"Transaction #{number}")

                print(
                    "Type        :",
                    transaction["transaction_type"]
                )

                print(
                    "Amount      : ₹",
                    transaction["amount"]
                )

                print(
                    "Description :",
                    transaction["description"]
                )

            print("--------------------------------")

    except ValueError as error:

        print("\nError:", error)


# ==========================================
# USER MENU
# ==========================================

def user_menu(account_number):

    while True:

        print("\n================================")
        print("          USER MENU")
        print("================================")

        print("1. Add Money")
        print("2. Check Balance")
        print("3. Transfer Money")
        print("4. Transaction History")
        print("5. Logout")

        choice = input(
            "\nEnter your choice: "
        )

        # Add Money
        if choice == "1":

            add_money_menu(account_number)

        # Check Balance
        elif choice == "2":

            check_balance_menu(account_number)

        # Transfer Money
        elif choice == "3":

            transfer_money_menu(account_number)

        # Transaction History
        elif choice == "4":

            transaction_history_menu(account_number)

        # Logout
        elif choice == "5":

            print("\nLogged out successfully.")
            print("Thank you for using our Banking System.")

            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number from 1 to 5.")


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    while True:

        print("\n")
        print("========================================")
        print("          SIMPLE BANKING SYSTEM")
        print("========================================")

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        # Create Account
        if choice == "1":

            create_account_menu()

        # Login
        elif choice == "2":

            login_menu()

        # Exit
        elif choice == "3":

            print("\n================================")
            print("Thank you for using our")
            print("Simple Banking System!")
            print("================================")

            break

        else:

            print("\nInvalid choice.")
            print("Please enter 1, 2, or 3.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main_menu()