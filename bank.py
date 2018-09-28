


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

# class User:
#     def __init__(self, first_name,last_name,middle_name):
#         self.bank_accounts = []

#         user = User(.....,...,...)-->pass this in the BankAccount class


#-----------------------------
funds = []
#accounts = []
users = []
balance = []
status_of_account = ["OPEN","CLOSED","FREEZE"]
user_id_count = 1
account_id_count = 1

def print_menu():
    print("Welcome to Pam's Bank!")
    print("1.Open bank account")
    print("2.Transfer funds")
    print("3.Withdraw funds")
    print("4.Fees and regulations")
    print("5.EXIT")

class User:
    def __init__(self,first_name,last_name,middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.accounts = []
        self.id = user_id_count
    def __repr__(self):
        return  '%s %s %s - %s' % (self.first_name, self.middle_name, self.last_name, self.accounts)

class BankAccount:
    def __init__(self,account_type,balance,status):
        self.account_type = account_type
        self.balance = balance
        self.status = status
        self.account_id = account_id_count
        #self.total = 0
    def __repr__(self):
        return  '%s %s, %s' % (self.account_type, self.balance, self.status)

def withdraw(account_selection,with_amount):
    new_balance = account_selection.balance - with_amount
    if new_balance < 0:
        new_balance = account_selection.balance - 35
        print("Insufficient funds!!-$35.00 overdraft fee applied.")
        print(f"Your new balance is {new_balance}")
        return new_balance
    else:
        print(f"Your new balance is {new_balance}")
        return new_balance

    # account_selection = input("Please select the account: ")
    # print(self.accounts)
    # if (account_selection =="1" "2","3"):
    #     return self.accounts[account_selection]
    # print("Current balance:" ,self.accounts.balance)
    # with_amount = int(input("How much would you like to withdraw: "))
    # if (with_amount < self.balance):
    #     self.balance -= with_amount
    #     print("New balance:",self.balance)
    #     print("******************************************")

    # else:
    #     self.balance -= with_amount
    #     self.balance -= 35
    #     print("Insufficient funds!!-$35.00 overdraft fee applied. Refer to fees and regulations for more info.")
    #     print("New balance: ",self.balance)
    #     self.status = status_of_account[2] 

def open_account():
    account_type = input("Enter type of account: ")
        
    balance = int(input("Enter current balance: "))
    if(balance < 100):
        print("Unable to open bank account. Please refer to -Fees and Regulations- on the main menu for more info!")
        pass
    else:
        global user
        status = status_of_account[0]
        bank_account = BankAccount(account_type,balance,status)
        user.accounts.append(bank_account)
        print(user)
        new_account_open()

def new_account_open():
    new_account = input("Enter (y) if you would like to open another account or press (any key) to exit: ")
    if new_account == "y":
        open_account()

    else:
        pass
        


#bank_account = BankAccount("Savings",5000,"OPEN")
#user = User("Obi","Ezeakachi","Oko")
#user.accounts.append(bank_account)

#b2 = BankAccount("Tasha","Tomas","KI",8000)
#b3 = BankAccount("Obi","Ezeakachi","Oko",7000)


loop = True
while loop:
    print_menu()
    option = (input("Please select an option [1-5]: "))
    if (option == "1"):
        print("*Option 1 has been selected*")
        first_name = input("Enter first name: ")
        middle_name = input("Enter middle name: ")
        last_name = input("Enter last name: ")
        account_type = input("Enter type of account: ")
        
        balance = int(input("Enter current balance: "))
        if(balance < 100):
            print("Unable to open bank account. Please refer to -Fees and Regulations- on the main menu for more info!")
            pass
        else:
            status = status_of_account[0]
            user = User(first_name,middle_name,last_name)
            user_id_count += 1
            users.append(user)
            bank_account = BankAccount(account_type,balance,status)
            account_id_count += 1
            user.accounts.append(bank_account)
            print(user)
        new_account_open() 
       
        
        
    elif (option == "2"):
        print("*Option 2 has been selected*")

    elif(option == "3"):
        print("*Option 3 has been selected*")
        user_id = int(input("Enter the User ID that owns the account: "))
        for user in users:
            if user.id == user_id:
                list_of_accounts = user.accounts
        account_to_withdraw = int(input("What is the ID of the account? "))
        for account in list_of_accounts:
            if account.account_id == account_to_withdraw:
                chosen_account = account
        amount_to_withdraw = int(input("How much would you like to withdraw? $"))
        withdraw(chosen_account, amount_to_withdraw)  
    elif(option == "4"):
        print("*Option 4 has been selected*")
        print("To open a bank account --> Initial balance has to be minumum $100.00")
        print("If bank account balance is lower than $0.00 --> Account will be charged an ovedraft fee of $35.00")
        question4 = input("Please press (b) to go back to the main menu: ")
        if (question4 == "b"):
            continue
    elif(option == "5"):
        print("*Option 5 has been selected*")
        print("Thank you for using our bank app!")
        loop = False
    else:
        input("Wrong option selection. Enter any key to try again... ")
    
   

