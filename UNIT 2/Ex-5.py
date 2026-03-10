class Bank:
    def __init__(self,pin,acount_number,balance):
        self.pin=pin
        self.acount_number=acount_number
        self.balance=balance
    def deposit(self,Mpin,acount_number,amount):
        self.Mpin=Mpin
        self.amount=amount
        self.acount_number=acount_number
        if self.pin==self.Mpin:
            self.balance+=self.amount
            print("Updated Balancer:",self.balance)
        else:
            print("Wrong Pin.")
    def withdraw(self,Mpin,acount_number,amount):
        self.Mpin=Mpin
        self.acount_number=acount_number
        self.amount=amount
        if self.pin==self.Mpin and self.balance>self.amount:
            self.balance-=self.amount
            print("Updated Balance:",self.balance)
        else:
            print("Wrong Pin or Insufficient balance.")
    def check_balance(self,Mpin,acount_number):
        self.Mpin=Mpin
        self.acount_number=acount_number
        if self.pin==self.Mpin:
            print(self.balance)
        else:
            print("Wrong Pin.")
while True:
    pin=int(input("Enter pin:"))
    acount_number=int(input("Enter acount number:"))
    balance=int(input("Enter balance:"))
    a=Bank(pin,acount_number,balance)
    choice=int(input('''1.Deposit
2.Withdraw
3.Check balance
choose anyone for operation.'''))
    if choice==1:
        Mpin=int(input("Enter Pin:"))
        acount_number=int(input("Enter acount number:"))
        amount=int(input("Enter desired amount to deposit:"))
        a.deposit(Mpin,acount_number,amount)
    elif choice==2:
        Mpin=int(input("Enter Pin:"))
        acount_number=int(input("Enter acount number:"))
        amount=int(input("Enter desired amount to withdraw:"))
        a.withdraw(Mpin,acount_number,amount)
    elif choice==3:
        Mpin=int(input("Enter Pin:"))
        acount_number=int(input("Enter acount number:"))
        a.check_balance(Mpin,acount_number)
    else:
        print("Invalid Choice.")
    op=input("Enter (Y/y) for continue and (N/n) for stop:")
    if op=='Y' or op=='y':
        continue
    else:
        break
