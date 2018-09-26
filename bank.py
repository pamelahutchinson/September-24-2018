


#------------------------(Example made in class):
# bankaccount

# -balance
# -type(checking/saving)
# -accountnumber
# -routing number
# -isOpen true/false

# transfer (amountToTransfer,from,to):
#     balance -= amountToTransfer

# close():
#     isOpen = false

#-----------------------------
funds = []

def print_menu():
    print("Welcome to Pam's Bank!")
    print("1.Open bank account")
    print("2.Transfer funds")
    print("3.Withdraw funds")
    print("4.Fees and regulations")
    print("5.EXIT")

class BankAccount:
    def __init__(self,first_name,last_name,middle_name,balance,):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        #self.account_type = account_type
        self.balance = balance
        #self.status = status

def withdraw(self):
    print("Current balance:" ,self.balance)
    with_amount = int(input("How much would you like to withdraw: "))
    if (with_amount < self.balance):
        self.balance -= with_amount
        print("New balance = ",self.balance)
        print("******************************************")
    else:
        print("Insufficient funds!!! Please try again.")
        withdraw(b1)




b1 = BankAccount("Obi","Ezeakachi","Oko",5000)
b2 = BankAccount("Tasha","Tomas","KI",8000)
b3 = BankAccount("Obi","Ezeakachi","Oko",7000)


loop = True
while loop:
    print_menu()
    option = int(input("Please select an option [1-5]: "))
    
    if (option == 1):
        print("*Option 1 has been selected*")
        first_name = input("Enter first name: ")
        middle_name = input("Enter middle name: ")
        last_name = input("Enter last name: ")
        
        minumun_balance = int(input("Enter current balance: "))
        if(minumun_balance < 100):
            print("Unable to open bank account. Please refer to -Fees and Regulations- on the main menu for more info!")
            continue

    elif (option ==2):
        print("*Option 2 has been selected*")
    elif(option == 3):
        print("*Option 3 has been selected*")
        withdraw(b1)  
    elif(option == 4):
        print("*Option 4 has been selected*")
        print("To open a bank account --> Initial balance has to be minumum $100.00")
        print("If bank account balance is lower than $0.00 --> Account will be charged an ovedraft fee of $35.00")
        question4 = input("Please press (b) to go back to the main menu: ")
        if (question4 == "b"):
            continue
    elif(option == 5):
        print("*Option 5 has been selected*")
        print("Thank you for using our bank app!")
        loop = False
    else:
        input("Wrong option selection. Enter any key to try again... ")
    
   

