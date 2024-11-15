# account_ui.py

from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository
from exceptions.exceptions import *

class AccountUI:
    def __init__(self):
        self.account_repository = AccountRepository()

    def start(self):
        while True:
            print('\nWelcome to Global Digital Bank')
            print('\nSelect an option:')
            print('1. Open Account')
            print('2. Close Account')
            print('3. Withdraw Funds')
            print('4. Deposit Funds')
            print('5. Transfer Funds')
            print('6. Display Accounts')
            print('8. Account Settings')
            print('9. Exit')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                self.open_account()
            elif choice == 2:
                self.close_account()
            elif choice == 3:
                self.withdraw_funds()
            elif choice == 4:
                self.deposit_funds()
            elif choice == 5:
                self.transfer_funds()
            elif choice == 6:
                self.display_account()
            elif choice == 8:
                self.account_settings()
            elif choice == 9:
                break
            else:
                print('Invalid choice. Please try again')



    def open_account(self):
        account_type = input('Enter account type (savings/current): ').strip().lower()
        name = input('Enter your name: ')
        amount = float(input('Enter initial deposit amount: '))
        pin_number = int(input('Enter your pin number: '))
        privilege = input('Enter account privilege (PREMIUM/GOLD/SILVER): ').strip().upper()

        if account_type == 'savings':
            date_of_birth = input('Enter your date of birth (YYYY-MM-DD): ')
            gender = input('Enter your gender (M/F): ')
            account = AccountManager().open_account(account_type, name=name, balance=amount,
            date_of_birth=date_of_birth, gender=gender, pin_number=pin_number, privilege=privilege)

        elif account_type == 'current':
            registration_number = input('Enter your registration number: ')
            website_url = input('Enter your website URL: ')
            account = AccountManager().open_account(account_type, name=name, balance=amount, 
            registration_number=registration_number, website_url=website_url, pin_number=pin_number,
            privilege=privilege)

        else:
            print('Invalid account type. Please try again')
            return

        print(account_type.capitalize(), 'Account opened successfully. Account Number: ',account.account_number)

 
    def close_account(self):
        account_number = int(input('Enter your account number: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().close_account(account)
                print('Account closed successfully')
            except Exception as e:
                print("Error: ", e)
        else:
            print('Account Not Found. Please try again')

    def withdraw_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input('Enter amount to withdraw: '))
        pin_number = int(input('Enter your pin number: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().withdraw(account, amount, pin_number)
                print('Amount withdrawn successfully')
            except Exception as e:
                print('Error: ', e)
        else:
            print('Account Not Found. Please try again')

    def deposit_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input('Enter amount to deposit: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().deposit(account, amount)
                print('Amount deposited successfully')
            except Exception as e:
                print('Error: ', e)
        else:
            print('Account Not Found. Please try again')

    def transfer_funds(self):
        from_account_number = int(input('Enter your account number: '))
        to_account_number = int(input('Enter recipient account number: '))
        amount = float(input('Enter amount to transfer: '))
        pin_number = int(input('Enter your pin number: '))

        from_account = next((acc for acc in AccountRepository.accounts if acc.account_number == from_account_number), None)
        to_account = next((acc for acc in AccountRepository.accounts if acc.account_number == to_account_number), None)

        if from_account and to_account:
            try:
                AccountManager().transfer(from_account, to_account, amount, pin_number)
                print('Amount transferred successfully')
            except Exception as e:
                print('Error: ', e)
        else:
            print('One or Both Account(s) Not Found. Please try again')

    def toggle_account_status(self):
        account_id = int(input("Enter the account ID: ").strip())
        status = input("Enter 'activate' to activate or 'inactivate' to deactivate: ").strip().lower()
        active = (status == "activate")
        AccountManager().set_account_status(account_id, active)
        print(f"Account {account_id} {'activated' if active else 'inactivated'}.") 

    def edit_account_details(self):
        # self.manager = AccountManager()
        account_id = int(input("Enter the account ID: ").strip())
        account = AccountRepository().get_account_by_id(account_id)
        if account.is_active:
            existing_pin_number = int(input('Enter your existing pin number: '))
            new_pin_number = int(input('Enter your new pin number: '))
            # name = input('Enter your name: ')
            AccountManager().set_account_details(account_id,new_pin=new_pin_number,current_pin=existing_pin_number)
            print(f"Account {account_id} details updated successfully.")
            self.account_repository.get_account_by_id(account_id)
        else:
            print("Account not active.")

    def account_settings(self):
        edit_type = input("Enter 'edit' for edit account details or 'toggle' for toggle account status : ").strip().lower()

        if edit_type == 'edit':
            self.edit_account_details()
        elif edit_type == 'toggle':
            self.toggle_account_status()

    def display_account(manager):
        try:
            choice = input("Enter 'type' to view by type, 'id' to view by ID, or press Enter to view all: ").strip().lower()
            if choice == "type":
                account_type = input("Enter account type (Savings/Current): ").strip()
                accounts = AccountManager().view_account(account_type=account_type)
            elif choice == "id":
                account_id = input("Enter account ID: ").strip()
                account = AccountManager().view_account(account_id=account_id)
                print(account)  # Single account (not a list)
                return
            else:
                accounts = AccountManager().view_account()

            # Display account details for multiple accounts
            if accounts:
                for account in accounts:
                    print(account)
            else:
                print("No accounts found.")
        except AccountDoesNotExistsException as e:
            print(str(e))
