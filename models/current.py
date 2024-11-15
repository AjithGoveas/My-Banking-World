#Current.py
from models.account import Account

class Current(Account):
    def __init__(self, name, balance, registration_number, website_url, pin_number, privilege):
        super().__init__(name, balance, pin_number, privilege)
        self.registration_number = registration_number
        self.website_url = website_url

    def __str__(self):
        return f"Current Account(ID: {self.account_number}, Balance: {self.balance}, Active: {self.is_active})"