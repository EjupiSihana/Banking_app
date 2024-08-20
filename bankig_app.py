import base_model

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
   
         
        
bankingApp = BankingApp()
bankingApp.start()
        
