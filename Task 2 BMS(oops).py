class Bank_Account:
    generate_no = 10001
    accounts={}
    def __init__(self, name, ini_amount, pin, mobile):
        self.name = name
        self.balance = ini_amount
        self.acc_no = Bank_Account.generate_no
        self.mobile = mobile
        self.pin = pin
        self.accounts = {}
        self.accounts[self.acc_no] = self
        Bank_Account.generate_no += 1
   
   
    def view_database():
        print("Bank Account Database:")
        for acc_no, account_obj in Bank_Account.accounts["acc_no"]:
            print(f"Account Number: {acc_no}")
            account_obj.details()
            print("\n")
    def details(self):
        print(f'Name: {self.name}\t  Balance: {self.balance}\t Mobile: {self.mobile}\t Pin: {self.pin}')
        print("Account created successfully. Your account Number is", self.acc_no)

    def deposit(self, acc_no, pin, amount):
        if acc_no == self.acc_no and pin == self.pin:
            if amount > 0:
                self.balance += amount
                print("Deposit successful!")
            else:
                print("Invalid Amount!")
        else:
            print("Transaction Failed! Invalid Account Credentials.")
        print("Your New Balance is:", self.balance)

    def withdraw(self, acc_no, pin, amount):
        if acc_no == self.acc_no and pin == self.pin:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful!")
            else:
                print("Invalid Amount or Insufficient Balance!")
        else:
            print("Transaction Failed! Invalid Account Credentials.")
        print("Your New Balance is:", self.balance)

    def check_balance(self, acc_no, pin):
        if acc_no == self.acc_no and pin == self.pin:
            print("Your Balance is:", self.balance)
        else:
            print("Transaction Failed! Invalid Account Credentials.")

if __name__ == "__main__":
    val = False
    print("Welcome to Bank Management System")
    while not val:
        print("1. Create New Account:")
        print("2. Deposit Money")
        print("3. Withdraw Money:")
        print("4. Check Balance:")
        print("5. see data:")
        print("6. Exit:")
        option = int(input("Enter your choice: "))

        if option == 1:
            name = input("Enter your Name: ")
            ini_amount = float(input("Enter the Initial amount to deposit: "))
            pin = input("Enter Your Pin: ")
            mobile = input("Enter your Mobile No.: ")
            account = Bank_Account(name, ini_amount, pin, mobile)
            account.details()

        elif option == 2:
            accno = int(input("Enter your Account no.: "))
            p = input("Enter pin: ")
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(accno, p, amount)

        elif option == 3:
            accno = int(input("Enter your Account no.: "))
            p = input("Enter pin: ")
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(accno, p, amount)

        elif option == 4:
            accno = int(input("Enter your Account no.: "))
            p = input("Enter pin: ")
            account.check_balance(accno, p)
        elif option==5:
            Bank_Account.view_database()
        elif option == 6:
            val = True
