import random


def generate_account_number(existing_accounts):

    while True:

        account_number = str(random.randint(100000, 999999))

        if account_number not in existing_accounts:
            return account_number