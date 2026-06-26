class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def credit(self , amount):
        self.balance +=amount
        print("Rs",amount,"was credited")
        print("total balance =", self.get_balance())

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000 , 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(1000)
acc1.debit(300)

        