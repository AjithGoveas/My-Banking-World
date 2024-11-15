from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
# from exceptions.exceptions import AccountNotActiveException
# from exceptions.exceptions import InsufficientFundsException
# from exceptions.exceptions import InvalidPinException
# from exceptions.exceptions import TransferLimitExceededException
from exceptions.exceptions import *
from services.transaction_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager

class AccountManager:

    def open_account(self, account_type, **kwargs):
        if account_type == 'savings':
            new_account = Savings(**kwargs)
        elif account_type == 'current':
            new_account = Current(**kwargs)
        else:
            raise ValueError('Invalid account type')

        AccountRepository.save_account(new_account)
        return new_account

    def check_account_active(self, account):
        if not account.is_active:
            raise AccountNotActiveException('Account is not Active')

    def validate_pin(self, account, pin_number):
        if account.pin_number != pin_number:
            raise InvalidPinException('Invalid Pin')

    def withdraw(self, account, amount, pin_number):
        self.check_account_active(account)
        self.validate_pin(account, pin_number)

        if account.balance < amount:
            raise InsufficientFundsException('Insufficient funds')

        account.balance -= amount
        TransactionManager.log_transaction(account.account_number, amount, 'withdraw')

    def deposit(self,account, amount):
        self.check_account_active(account)

        account.balance += amount
        TransactionManager.log_transaction(account.account_number, amount, 'deposit')

    def transfer(self, from_account, to_account, amount, pin_number):
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account, pin_number)

        if from_account.balance < amount:
            raise InsufficientFundsException('Insufficient funds')

        limit = AccountPrivilegesManager.get_transfer_limit(from_account.privilege)
        if amount > limit:
            raise TransferLimitExceededException('Transfer limit exceeded')

        from_account.balance -= amount
        to_account.balance += amount
        TransactionManager.log_transaction(from_account.account_number, amount, 'transfer', to_account.account_number)


    def close_account(self, account):
        if not account.is_active:
            raise AccountNotActiveException('Account is already Deactivated')
        

    # def view_account(self, account_repository, account_type=None, account_id=None, pin_number=None):
    #         if account_type:
    #             accounts = [acc for acc in account_repository.get_all_accounts() if acc.type == account_type]
    #             for account in accounts:
    #                 self.check_account_active(account)  # Check if each account is active
    #             return accounts

    #         elif account_id:
    #             account = account_repository.get_account_by_id(account_id)
    #             if account:
    #                 self.check_account_active(account)  # Ensure the account is active
    #                 if pin_number is not None:  # If a PIN is provided, validate it
    #                     self.validate_pin(account, pin_number)
    #                 return account
    #             else:
    #                 raise AccountDoesNotExistsException("Account ID not found.")

    #         else:
    #             # View all accounts if no filter is provided
    #             accounts = account_repository.get_all_accounts()
    #             for account in accounts:
    #                 self.check_account_active(account)
    #             return accounts

    def set_account_status(self, account_id, active):
        account = AccountRepository().get_account_by_id(account_id)
        if account:
            account.is_active = active
            AccountRepository().update_account(account)
        else:
            raise AccountDoesNotExistsException("Account ID not found.")
        
    def set_account_details(self, account_id, name=None, new_pin=None, current_pin=None):
        account = AccountRepository().get_account_by_id(account_id)
        if account:
            # Validate current pin if provided (optional security check)
            if current_pin is not None and account.pin_number != current_pin:
                raise InvalidPinException("Current PIN is incorrect.")
            
            # Update account details based on provided arguments
            if name:
                account.name = name
            if new_pin:
                account.pin_number = new_pin
            
            # Save the updated account
            AccountRepository().update_account(account)
            print(f"Account {account_id} successfully updated.")
        else:
            raise AccountDoesNotExistsException("Account ID not found.")