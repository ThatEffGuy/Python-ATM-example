#ATM
#Craig Ferguson
#18/11/20

#libraries ie time, system

#methods    blocks of code

def welcomeScreen():
    print ("B A N K  O F  S C O T L A N D")
    print ("=============================")
    print ("    A T M   Withdraw Cash    ")
    print()

#End welcomescreen

def atm():
    balance = 100
    amount = int(input("Amount to withdraw : "))

    if amount > 300:
        print("Max Withdraw £300")
    elif amount > balance:
        print("insufficent funds")
    elif amount // 10 != amount / 10:
        print("not a multiple of 10")
    else:
        print("withdrawn £", amount)
    #end if



#end atm

def thankyou():
    print ("Thank you for your business")
    print ("Come back soon")

#main program

welcomeScreen()
atm()
thankyou()