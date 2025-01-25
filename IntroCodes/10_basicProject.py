import random as random

def check(ans):
    if ans == "y" or ans == "yes":
        return 1
    elif ans == "n" or ans == "no":
        return 0
    else:
        print("No valid Input, returning to the main section")
        return None

def check02(ans):
    try:
        ans=int(ans)
        return ans
    except:
        print("Invalid Input")
        return None

def question01():
    choices=input("""Welcome to the 'Broke' Bank, do you want to ...
            01. Logon to your account?
            02. Create and account?
            03. Verify a transaction?
            1/2/3: """)
    return choices

def supports():
    x= input("""What kind of supports can we provide to you?
            01.Balance Check
            02.Send Money
            03.Deposit
            04.Withdraw
            05.Account Profile
            """)
    try:
        x=int(x)
        return x
    except:
        return None

class Bank:
    use_pass={}
    id_name={}
    transaction=[]
    def __init__(self, name=None):
            firstName=input("Your first name: ").lstrip().rstrip()
            secondName=input("Your second name: ").lstrip().rstrip()
            lastName=input("Your last name: ").lstrip().rstrip()
            q2 = int(input("Enter your age: "))
            q3 = [int(i) for i in input("Enter your Date of Birth with a '/' between: ").split("/")]
            q4 = int(input("Give your NID number: "))
            id = random.randint(100000000000,999999999999)
            while id in Bank.id_name:
                id=random.randint(100000000000,999999999999)
            print(Bank.use_pass)
            Bank.id_name[id]=self
            self._name = firstName+" "+secondName+" "+lastName
            self._age = q2
            self._dob = q3
            self._nid = q4
            self._amount=0
            self._history=[]
            self._id=id
            password=input("Enter the password: ")
            password2=input("Re-enter the password: ")
            while password!=password2:
                print("Wrong match")
                password=input("Enter the password: ")
                password2=input("Re-enter the password: ")
            self._pass=password
            print("Account created")

    ##########################################################################################

    def get_id(self):
        return self._id

    ##########################################################################################

    def checkPass(self):
        password=input("Enter the password: ")
        return True if password==self._pass else False 
    
    ##########################################################################################

    def change_pass(self):
        if input()==self._pass:
            give_new=input()
            conf_new=input()
            if give_new==conf_new:
                self._pass=give_new
                print("Password updated Successfully")
            else:
                print("Gave both password that are not matched")
        else:
            print("Wrong Password...")

    ##########################################################################################

    def check_balance(self):
        print(f"Balance equity is {self._amount}")
    
    ##########################################################################################

    def deposit(self, amount):
        amount=check02(amount)
        if amount!=None:
            remark=input("If Any: ")
            if remark=="":
                remark="No Comment"
            self._amount+=amount
        else:
            print("Dont have characters or cents to pay with")

    ##########################################################################################

    def withdraw(self, amount):
        amount=check02(amount)
        if amount!=None and amount>0:
            remark=input("If Any Comment to give: ")
            if remark=="":
                remark="No Comment"
            if self._amount-amount>=0:
                self._amount-=amount
            else:
                print(f"You're {amount-self._amount} money short to withdraw")
        else:
            print("Dont have characters or cents or \"ZEROS\" to pay with")
        
    ##########################################################################################

    def transact(self,id=None,name=None,amount=0):
        amount=check02(amount)
        if amount!=None and amount>0:
            remark=input("If Any Comment to give: ")
            if remark=="":
                remark="No Comment"
            if id!=None:
                for i in Bank.id_name:
                    if i==id:
                        receiver=Bank.id_name[id]
                        if self._amount-amount>=0:
                            self._amount-=amount
                            print(f"Send {amount} This amount to Bank.")
                            receiver._amount+=amount
                            id = hex(random.randint(100000000000,999999999999))
                            while id in Bank.transaction:
                                id = hex(random.randint(100000000000,999999999999))
                            Bank.transaction.append((id,self._id,receiver._id,remark))
                            print(f"""The transaction Id: {hex(id)}
Sender: {self._id} and name is {self._name}
Receiver: {receiver._id} and name is {receiver.name}
Comments: {remark}""")
                            break
                    else: 
                        print("No sufficient balance")
                else:
                    print("ID not found")
            elif name!=None:
                for i in Bank.use_pass:
                    if i == name:
                        receiver=Bank.use_pass[name][0]
                        if self._amount-amount>=0:
                            self._amount-=amount
                            print(f"Send {amount} This amount to Bank.")
                            receiver._amount+=amount
                            id = hex(random.randint(100000000000,999999999999))
                            while id in Bank.transaction:
                                id = hex(random.randint(100000000000,999999999999))
                            Bank.transaction.append((id,self._id,self._name,receiver._id,receiver._name,remark))
                            print(f"""The transaction Id: {hex(id)}
Sender: {self._id} and name is {self._name}
Receiver: {receiver._id} and name is {receiver.name}
Comments: {remark}""")
                            break
                    else: 
                        print("No sufficient balance")
                else:
                    print("ID not found")
            else:
                print("No Data Given, No process is completed further")

    ##########################################################################################

    def send(self):
        amount=input("")
        ans=check02(input("Do you know ID?(0/1) "))
        if ans == 1:
            id=input("Give the ID of the user that you need to send the Money: ")
            self.transact(id,None,amount)
        elif ans ==0:
            ans=check02(input("Do you know the name of the receiver?(0/1) "))
            if ans ==1:
                name=input("Give the name: ")
                self.transact(None,name,amount)
        else:
            print("Sorry You have no valid information")
            self.transact()

    ##########################################################################################

    def transaction_print(self,transaction):
        for i in Bank.transaction:
            if i[0]==hex(transaction):
                index=i
                print(f"""The transaction Id: {index[0]}
Sender: {index[1]} and name is {index[2]}
Receiver: {index[3]} and name is {index[4]}
Comments: {index[5]}""")
                break
        else:
            print("No transaction history available, or the transaction is invalid")


    ##########################################################################################

    def account(self):
        print(f"""
Username: {self}
Name: {self._name}
Age: {self._age}
Date of Birth: {self._dob}
NID: {self._nid}
Bank ID: {self._id}
Balance: {self._amount}
""")

while True:
    print(Bank.use_pass)
    print("""
        ##############################
        Welcome to the Bank of Brokers
            The coder is the great one
        ##############################""")
    choice = check02(question01())
    while not choice:
        choice=check02(question01())
    username=input("Give the username: ")
    if choice==1:
        if  Bank.use_pass[username][0].checkPass()==True:
            print("Thank You...")
            x=1
            while x!=0:
                supp=supports()
                if supp==1:
                    Bank.use_pass[username][0].check_balance()
                elif supp==2:
                    Bank.use_pass[username][0].send()
                elif supp==3:
                    amm=check02(input("Enter the amount you wanna deposit: "))
                    Bank.use_pass[username][0].deposit(amm)
                elif supp==4:
                    amm=check02(input("Enter the amount you wanna withdraw: "))
                    Bank.use_pass[username][0].withdraw(amm)
                elif supp==5:
                    Bank.use_pass[username][0].account()
                else:
                    print("Wrong Input, Sorry, starts from 1-6")
                x=check(input("To log out, enter 0 (else you can give any value): "))

        else:
            print("Invalid username or password")
            continue
        
    elif choice==2:
        while True:
            if username!=None and len(username)>=4:
                temp=Bank(username)
                Bank.use_pass[username]=[temp]
                Bank.use_pass[username].append(Bank.use_pass[username][0].get_id())
                print(Bank.id_name,"\n",Bank.use_pass)
                break
            else:
                print("Give the name at least a length of 4.")
                username=""
                continue
            if opt==None:
                opt=supports()
                continue
            else:
                break

    elif choice==3:
        transaction_code=("Give the Transaction Number: ")
        Bank.use_pass[username].transaction_print(transaction_code)

    else:
        print("Hello")