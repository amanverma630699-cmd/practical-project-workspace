balance = 1000000
pin = 12345
def pin_check():
    pin = int(input("enter your pin:"))
    if pin == 12345:
        print("correct pin")
        def check_balance():
            if balance >= 1000:
                print("your balance is:",balance)
        
            else:
               print("false")
        check_balance()
    else:
        print("incorrect pin")
pin_check()
