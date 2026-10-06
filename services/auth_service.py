class AuthService:

    def __init__(self, repository):
        self.repository = repository

    def login(self, account_number, password):

        accounts = self.repository.load_accounts()

        if account_number not in accounts:
            raise ValueError("Account not found")

        account = accounts[account_number]

        if account["password"] != password:
            raise ValueError("Invalid password")

        return account_number