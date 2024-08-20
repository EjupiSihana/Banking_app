import base_model, enum

class BankingApp:
    def start(self):
        
        bank_account = base_model.Bank_Account()
        bank_account.set_account_number(1212121)
        bank_account.set_account_owner("Filan Fisteku")
        bank_account.set_account_balance(500.0)

        bank_account_owner = base_model.BankAccountOwner()
        bank_account_owner.set_first_name("Filan")
        bank_account_owner.set_last_name("Fisteku")

        bank_account.set_account_owner(bank_account_owner)
    def __init__(self):
        self.__bankAccount_array = []
    
    def get_bank_account_array(self):
        return self.__bankAccount_array
    
    def set_bank_account_array(self, bankAccount_array):
        self.__bankAccount_array = bankAccount_array

         
        print("Bank account with the corresponding number: " + bankAccount_array() "bolongs to:() " and it's " + bank_account_type() + bank_account)

bankingApp = BankingApp()
bankingApp.start()
        