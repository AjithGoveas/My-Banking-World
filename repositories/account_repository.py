# AccountRepository.py
from exceptions.exceptions import *   

class AccountRepository:
    # Class attribute to store all the elements
    accounts = []
    account_counter = 1000

    # Method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter

    # Method to save Account
    @classmethod
    def save_account(cls, account):
        cls.accounts.append(account)

    # Method to get all accounts
    def get_accounts(self):
        return self.accounts
    
    def get_account_by_id(self, account_id):
        # Search for the account by its ID
        for account in self.accounts:
            if account.account_number == account_id:  # Adjust based on your actual account object structure
                return account
        return None  # Return None if account is not found

    def get_account_by_type(self, account_type):
        # Return a list of accounts matching the specified type
        return [account for account in self.accounts if account['type'].lower() == account_type.lower()]
    
    def update_account(self, account):
        # Loop through accounts to find and update the target account
        for i, existing_account in enumerate(self.accounts):
            if existing_account.account_number == account.account_number:  # Dot notation for attribute access
                self.accounts[i] = account
                return
        raise AccountDoesNotExistsException("Account ID not found.")