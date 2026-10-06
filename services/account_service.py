from models.account import Account
from utils.account_number import generate_account_number
from utils.validators import validate_name, validate_password


class AccountService:

    def __init__(self, repository):
        self.repository = repository

    def create_account(self, name, password):

        name = validate_name(name)
        password = validate_password(password)

        accounts = self.repository.load_accounts()

        account_number = generate_account_number(accounts)

        account = Account(
            account_number,
            name,
            password,
            0
        )

        accounts[account_number] = {
            "name": account.name,
            "password": account.password,
            "balance": account.balance,
            "transactions": []
        }

        self.repository.save_accounts(accounts)

        return account_number