balance = 100000
pin = 1234
def pin_check():
    pin = int(input("enter your pin:"))
    if pin == 1234:
        print("right pin")
        return True
    else:
        print("wrong pin:")
        return False
pin_check()
def check_balance():
    if balance >= 0:
        print("your balance is:",balance)
    else:
        print("false")
check_balance()       

def withdraw():
    withdraw = int(input("enter your money you want:"))
    print("successfully withdraw")    
withdraw()   

def atm():
    print("===== WELCOME TO ATM =====")

if pin_check():

    while True:
        print("\n===== ATM MENU =====")
        print("1. check balance")
        print("2. withdraw")
        print("3. exit")
        choice = int(input("enter your choice:"))
        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            print("thank you for using atm")
            break
        else:
            print("invalid choice")
atm()