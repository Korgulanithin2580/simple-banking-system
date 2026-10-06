from models.transaction import Transaction


class TransactionService:

    def __init__(self, repository):
        self.repository = repository

    # ==========================================
    # CHECK BALANCE
    # ==========================================

    def check_balance(self, account_number):

        accounts = self.repository.load_accounts()

        if account_number not in accounts:
            raise ValueError("Account not found")

        return accounts[account_number]["balance"]

    # ==========================================
    # ADD MONEY
    # ==========================================

    def add_money(self, account_number, amount):

        accounts = self.repository.load_accounts()

        if account_number not in accounts:
            raise ValueError("Account not found")

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than 0"
            )

        account = accounts[account_number]

        # Add money to balance
        account["balance"] += amount

        # Create transaction
        transaction = Transaction(
            "DEPOSIT",
            amount,
            "Money added to account"
        )

        account["transactions"].append(
            transaction.to_dict()
        )

        # Save updated account
        self.repository.save_accounts(accounts)

    # ==========================================
    # TRANSFER MONEY
    # ==========================================

    def transfer(
        self,
        sender_account,
        receiver_account,
        amount
    ):

        accounts = self.repository.load_accounts()

        if sender_account not in accounts:
            raise ValueError(
                "Sender account not found"
            )

        if receiver_account not in accounts:
            raise ValueError(
                "Receiver account not found"
            )

        if sender_account == receiver_account:
            raise ValueError(
                "Cannot transfer to the same account"
            )

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than 0"
            )

        sender = accounts[sender_account]
        receiver = accounts[receiver_account]

        if sender["balance"] < amount:
            raise ValueError(
                "Insufficient balance"
            )

        # Transfer money
        sender["balance"] -= amount
        receiver["balance"] += amount

        # Sender transaction
        sender_transaction = Transaction(
            "TRANSFER",
            amount,
            f"Transfer to {receiver_account}"
        )

        # Receiver transaction
        receiver_transaction = Transaction(
            "RECEIVED",
            amount,
            f"Received from {sender_account}"
        )

        sender["transactions"].append(
            sender_transaction.to_dict()
        )

        receiver["transactions"].append(
            receiver_transaction.to_dict()
        )

        # Save changes
        self.repository.save_accounts(accounts)

    # ==========================================
    # TRANSACTION HISTORY
    # ==========================================

    def transaction_history(self, account_number):

        accounts = self.repository.load_accounts()

        if account_number not in accounts:
            raise ValueError(
                "Account not found"
            )

        return accounts[account_number]["transactions"]