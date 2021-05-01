class atm(object):
   def __init__(self, cardnumber, pin):
       self.cardnumber = cardnumber
       self.pin = pin
   def checkBlance(self):
       print("You have 3lakh money in ur bank account")
        
   def withdraw(self, amount):
        newAmount = 300000-amount       
        print("Your have withdrawn " + str(amount) + " inr From you bank balance, Your remaining bank balace is: " + str(newAmount))
def main():
    cardNumber = input("Type your card number: ")
    pinNumber = input("Type your pin number: ")
    new_user = atm(cardNumber, pinNumber)
    print("What you want to do?")
    print("1. Check Blance 2.withdraw money")
    print("type 1 or 2")
    act = int(input("Enter your activity: "))
    if(act==1):
        new_user.checkBlance()
    elif (act==2):
        ammount = int(input("Enter amount to withdraw: "))
        new_user.withdraw(ammount)
    else:
        print("Enter a valid activity number")
if __name__ == "__main__":
    main()    
