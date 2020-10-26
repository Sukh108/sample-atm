def recurse():
	balance=database[account]['balance']
	choice=int(input("please chose one option\n 1.view balance \n 2.withdraw \n 3.deposit \n 4. exit\n"))
	if choice == 1:
        	print('balance:',balance)
        	recurse()
	elif choice == 2:
	       	
          	amt=int(input("please enter amount"))
          	if amt <= balance:
          		
          		database[account]['balance']=balance-amt
        	  	print("withdraw succesful")
        	  	recurse()
          	else :
        	  	print("you don't have a sufficiant balance for withdraw")
        	  	recurse()
	elif choice == 3:
        	amt=input("please enter amount")
        	database[account]['balance']=balance+amt
        	recurse()
	elif choice == 4:
        	print("thankyou")
        
	else:
        	print("please enter a valid choice")
        	recurse()
database = {
    1001:{
        'name': 'Sukh',
        'age': 22,
        'email': 'sukj000@gmail.com',
        'password': 'sukh123',
        'balance':20000
    },
    1002:{
        'name': 'mayank',
        'age': 25,
        'email': 'mayank@gmail.com',
        'password': 'maya123',
        'balance':10000
    }
}

account = int(input("Enter account number: "))
passwd = input("Enter password: ")
balance=database[account]['balance']

if account in database.keys():
    if passwd == database[account]['password']:
        print(f"Login Success\nWelcome {database[account]['name']}")
        
    
        choice=int(input("please chose one option\n 1.view balance \n 2.withdraw \n 3.deposit \n 4. exit\n"))
        if choice == 1:
        	print('balance:',balance)
        	recurse()
        elif choice == 2:
        	amt=int(input("please enter amount"))
        	if amt <= balance:
        		database[account]['balance']=balance-amt
        		print("withdraw succesful")
        		recurse()
        	else :
        		print("you don't have a sufficiant balance for withdraw")
        		recurse()
        	
        elif choice == 3:
        	amt=int(input("please enter amount"))
        	database[account]['balance']= balance + amt
        	recurse()
        	
        elif choice == 4:
        	print("thankyou")
        	
        else:
        	print("please enter a valid choice")
        	recurse()
       
        
        	
     
    else:
        print("Password FAiled")
else:
    print("Account is Not Exist")

   
