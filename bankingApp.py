from model import Bank, Bank_Account, BankAccountOwner

class BankingApp:
    def start(self):
        bank = Bank()
        bank.set_name("XYZ")
        bank.set_address("123")

        bank_account_owner1 = BankAccountOwner()
        bank_account_owner1.set_first_name("B")
        bank_account_owner1.set_last_name("A")
        
        account1 = Bank_Account()
        account1.set_account_number(123456)
        account1.set_accountOwner(bank_account_owner1)
        account1.set_bank(bank)

        bank_account_owner2 = BankAccountOwner()
        bank_account_owner2.set_first_name("C")
        bank_account_owner2.set_last_name("H")

        account2 = Bank_Account()
        account2.set_account_number(198745)
        account2.set_accountOwner(bank_account_owner2)
        account2.set_bank(bank)

        bank_account_owner3 = BankAccountOwner()
        bank_account_owner3.set_first_name("S")
        bank_account_owner3.set_last_name("ZH")

        account3 = Bank_Account()
        account3.set_account_number(52465)
        account3.set_accountOwner(bank_account_owner3)
        account3.set_bank(bank)

        bank_account_array = []
        bank_account_array.append(account1)
        bank_account_array.append(account2)
        bank_account_array.append(account3)

        print("Using for loop:")
        for i in range (0,3):
            account = (bank_account_array[i])
            print("Bank account with the corresponding number " + str(account.get_account_number()) + " belongs to " + account.get_accountOwner().get_first_name() + account.get_accountOwner().get_last_name())
        
        print("Using for-each")

        account : Bank_Account
        for account in bank_account_array:

             print("Bank account with the corresponding number " + str(account.get_account_number()) + " belongs to " + account.get_accountOwner().get_first_name() + account.get_accountOwner().get_last_name())

        i = 0
        array_length = 3
        print("Using while loop")
        while(i<array_length):
            account = (bank_account_array[i])
            print("Bank account with the corresponding number " + str(account.get_account_number()) + " belongs to " + account.get_accountOwner().get_first_name() + account.get_accountOwner().get_last_name())
            i = i + 1

bankingApp = BankingApp()
bankingApp.start()