class Bank:
   
    bank_name = "Default Bank"

   
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()


print("Initial Bank Names:")
print("Bank 1:", bank1.bank_name)
print("Bank 2:", bank2.bank_name)


Bank.change_bank_name("Global Trust Bank")

print("\nAfter Changing Bank Name:")
print("Bank 1:", bank1.bank_name)
print("Bank 2:", bank2.bank_name)
