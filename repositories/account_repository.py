import json
import os


class AccountRepository:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_accounts(self):

        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r") as file:

            try:
                accounts = json.load(file)

                # Make sure accounts is a dictionary
                if not isinstance(accounts, dict):
                    return {}

                return accounts

            except json.JSONDecodeError:
                return {}

    def save_accounts(self, accounts):

        with open(self.file_path, "w") as file:
            json.dump(
                accounts,
                file,
                indent=4
            )