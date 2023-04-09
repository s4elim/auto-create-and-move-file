class Banksystem:
    def __init__(self):
        
        self.account_info = {123:[1321,'Selim','male','01788082070',500]}
        

    def create_account(self,name,gender,phone,id,password,amount=0):
        self.id = id
        self.password = password
        self.name = name
        self.gender = gender
        self.phone = phone
        self.amount = amount

        self.account_info[self.id] = [self.password,self.name,self.gender,self.phone,self.amount]




    def account_informetion(self,id,password):
        if id == 1321 and password == 1321:
            for item in self.account_info:
                print('\n**************Name : {}. ****************\n'.format(self.account_info[item][1]))
                
                print( 'ID : {} \t\t\tGender :{}.'.format(item,self.account_info[item][2]))
                print('Phone :{} \t\tBalance :{} Taka.'.format(self.account_info[item][3],self.account_info[item][4]))
                
                print('\n********************************************\n')
        else:
            print('sorry sir pleace try again')



    def deposit_amount(self,id,amount):
        for item in self.account_info:
            if item == id:
                self.account_info[item][4] = self.account_info[item][4] + amount
                print('Deposite success.\nBalance {} Taka.'.format(self.account_info[item][4]))
                
                

    def withdraw(self,id,amount):
        for item in self.account_info:
            if item == id:
                if self.account_info[item][4] >= 0:
                    self.account_info[item][4] = self.account_info[item][4] - amount
                    print('Credite success.\nBalance {} Taka.'.format(self.account_info[item][4]))
     
                else:
                    print('Sorry you do not have sufficiency balance')


    def balance_amount(self,id):
        for item in self.account_info:
            if item == id:
                print('Name : {}.\nBalance : {} Taka.'.format(self.account_info[item][1],self.account_info[item][4]))
        


    def idpass(self,id,passwoed):
        for item in self.account_info:
            if item == id and self.account_info[item][0]:
                print('Log in Successfully')
                while True:
                    input_user_choice = int(input('Enter 1 for Account Balance, 2 for Withdraw Balance, 3 for deposit Balance, 4 for log out.:'))
                    if input_user_choice == 1:
                                            self.balance_amount(id)
                                            print('\n********************************************\n')

                    elif input_user_choice == 2:
                                            amount = int(input('Enter amount :'))
                                            self.withdraw(id,amount)
                                            print('\n********************************************\n')

                    elif input_user_choice == 3:
                                            amount = int(input('Enter amount :'))
                                            self.deposit_amount(id,amount)
                                            print('\n********************************************\n')

                                
                    elif input_user_choice == 4:
                        break

                    else:
                        print('Something wrong, pleace try again')
                        print('\n********************************************\n')




while True:
    a = Banksystem()
    input_ = int(input('Enter 1 for Create Account, 2 for admin login,3 for user login 4 for cancel system : '))
        print('\n********************************************\n')

    if input_ == 1:
        name = str(input('Enter your name : '))
        gender = str(input('Enter your gender : '))
        phone  = str(input('Enter your phone number : '))
        id = int(input('Enter your id number : '))
        password = int(input('Enter your Password : '))
        a.create_account(name,gender,phone,id,password)
        print('\n********************************************\n')



        
    elif input_ == 2:
        id = int(input('Enter admin id Number : '))
        password = int(input('Enter admin password : '))
        a.account_informetion(id,password)
        print('\n********************************************\n')

        

        
    elif input_ == 3:
        id = int(input('Enter Your id Number : '))
        password = int(input('Enter your password : '))
        a.idpass(id,password)
        print('\n********************************************\n')

        

    elif input_ ==4:
        break
    else:
        print('Something wrong')
