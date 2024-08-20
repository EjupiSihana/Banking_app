
class Bank_Account:

    def __init__(self):
        self.__account_number = int
        self.__account_owner = BankAccountOwner
        self.__balance = 0.0
        self.__MAXIMAL_WITHDRAW = 100.0
        self.__bank = str

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number
    
    def set_account_owner(self, account_owner):
        self.__account_owner = account_owner

    def get_account_owner(self):
        return self.__account_owner
    
    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance

    def get_account_balance(self):
        return self.__account_balance
    
    def set_bank(self, bank):
        self.__bank = bank

    def get_bank(self):
        return self.__bank
    
    def set_get_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def  get_deposite(self, amount):
        self.__balance +=amount

    def withdraw(self, amount):
        self.__balance -=amount
    
class BankAccountOwner:
    def __init__(self):
        self.__first_name = str
        self.__last_name = str

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name
