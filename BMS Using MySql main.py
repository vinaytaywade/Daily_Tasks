import mysql.connector


database = mysql.connector.connect(host="localhost", user="root", passwd="$sql2OPEN$", database="vinaydb")


cursorObject = database.cursor()


bank_record = """CREATE TABLE IF NOT EXISTS bank (
                Acc INT(10) PRIMARY KEY,
                nam VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                balance BIGINT NOT NULL,
                pin INT(6) NOT NULL
                )"""
cursorObject.execute(bank_record)


class Bank_Account:
    generate_no = 10001

    def __init__(self, nam, ini_amount, pin):
        self.nam = nam
        self.age = 0
        self.balance = ini_amount
        self.pin = int(pin)
        self.acc_no = Bank_Account.generate_no
        Bank_Account.generate_no += 1

        while self.check_account_exists(self.acc_no):
            self.acc_no = Bank_Account.generate_no
            Bank_Account.generate_no += 1

        B_acc = "INSERT INTO bank (Acc, nam, age, balance, pin) VALUES (%s, %s, %s, %s, %s)"
        values = (self.acc_no, self.nam, self.age, self.balance, self.pin)
        cursorObject.execute(B_acc, values)
        database.commit()


    def deposit(self,acc_no,pin):
        print("deposit")
        if acc_no == self.acc_no and pin == self.pin:
            if amount > 0:
                self.balance += amount
                update_query = "UPDATE bank SET balance = %s WHERE Acc = %s"
                values = (self.balance, self.acc_no)
                cursorObject.execute(update_query, values)
                database.commit()
                print(f"Deposited ${amount}. New balance: ${self.balance}")
            else:
                print("Invalid deposit amount. Amount must be greater than zero.")
        else:
            print("Transaction Failed! Invalid Account Credentials.")

    def withdraw(self, acc_no, pin, amount):
        if acc_no == self.acc_no :#and pin == self.pin:
            if 0 < amount <= self.balance:
                self.balance -= amount
                update_query = "UPDATE bank SET balance = %s WHERE Acc = %s"
                values = (self.balance, self.acc_no)
                cursorObject.execute(update_query, values)
                database.commit()
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Invalid Amount or Insufficient Balance!")
        else:
            print("Transaction Failed! Invalid Account Credentials.")

    def check_balance(self):
        print(f"Your Balance is: ${self.balance}")

    def view_database():
        cursorObject.execute("SELECT * FROM bank")
        records = cursorObject.fetchall()
        if not records:
            print("No records found.")
        else:
            print("Bank Records:")
            for record in records:
                print("Account Number:", record[0])
                print("Name:", record[1])
                print("Age:", record[2])
                print("Balance:", record[3])
                print("PIN:", record[4])
                print("==========================")

    @staticmethod
    def check_account_exists(acc_no):
        cursorObject.execute("SELECT Acc FROM bank WHERE Acc = %s", (acc_no,))
        record = cursorObject.fetchone()
        return record is not None

if __name__ == "__main__":
    print("Welcome to Bank Management System")
    while True:
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. See Data")
        print("6. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            nam = input("Enter your Name: ")
            ini_amount = float(input("Enter the Initial amount to deposit: "))
            pin = int(input("Enter Your PIN: "))
            account = Bank_Account(nam, ini_amount, pin)
            print("Account created successfully")
        elif option == 2:
            acc_no = int(input("Enter your Account no.: "))
            pin = input("Enter PIN: ")
            b = Bank_Account.deposit(acc_no, pin, amount)
            print(b)
        elif option == 3:
            acc_no = int(input("Enter your Account no.: "))
            pin = input("Enter PIN: ")
            amount = float(input("Enter the amount to withdraw: "))
            Bank_Account.withdraw(acc_no, pin, amount,amount)
        elif option == 4:
            Bank_Account.check_balance()
        elif option == 5:
            Bank_Account.view_database()
        elif option == 6:
            break
