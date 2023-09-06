accounts ={}
generate_account_no = 1000000000  
def generate_unique_account_number():
    global generate_account_no
    generate_account_no += 1
    return generate_account_no 
def create_account():
    name=input("Enter your Name :") 
    account_no=generate_unique_account_number()
    pin=int(input("Enter your 6 digit PIN number: "))
    balance=float(input("Enter balance to your account "))        
    accounts_info ={
        'Name' : name,
        'Account Number':account_no,
        'PIN':pin,
        'Balance': balance
    }
    accounts[account_no]=accounts_info
    print("\n Account created succesfully:")
    print("Your Account number is:",account_no)

    
def deposit():
    accountno=int(input("Enter your Account number:")) 
    if accountno in accounts:
        pin_no=int(input("Enter your pin:"))
        if pin_no == accounts[accountno]["PIN"]: 
            deposit=float(input("Enter amount to deposit:"))
            if deposit>0:
                 accounts[accountno]["Balance"]+=deposit
            else :
                print("Invalid Deposit amount")
                
        else:
            print("Invalid pin")
    else:
        print("Account number not found")           
    print("Deposit successful! Your current balance is:",accounts[accountno]["Balance"])

def check_balance():  
    accountno=int(input("Enter your Account number:")) 
    if accountno in accounts:
        pin_no=int(input("Enter your pin:"))
        if pin_no == accounts[accountno]["PIN"]:
            print("Your current balance is: ",accounts[accountno]["Balance"])
        else:
            print("Invalid pin number! Transaction Failed")
    else:
        print("Invalid account number! Transaction Failed")


def withdraw(): 
    accountno=int(input("Enter your Account number:")) 
    if accountno in accounts:
        pin_no=int(input("Enter your pin:"))
        if pin_no ==accounts[accountno]["PIN"]:
            withdraw= float(input("Enter the amount to withdraw:"))
            if withdraw <= accounts[accountno]["Balance"] and withdraw>0:
                accounts[accountno]["Balance"] -= withdraw
            else:
                print("You have entered Invalid amount!")
        else:
            print("Invalid pin number! Transaction Failed")
    else:
        print("Invalid account number! Transaction Failed")
    print("Your current balance is:",accounts[accountno]["Balance"])


val=False
print("Welcome to Bank Management System")
while val!=True:
    
    print("1.Create New Account:")
    print("2.Deposit Money")
    print("3.Withdraw Money:")
    print("4.Check Balance:")
    print("5.Exit:")
    option=int(input("Enter your choice:"))

    if option==1:
        create_account()
    if option ==2:
        deposit()
    if option ==3:
        withdraw()
    if option ==4:
        check_balance()
    if option==5:
        val=True


 