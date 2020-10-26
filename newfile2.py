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
        'name': 'Sachin',
        'age': 22,
        'email': 'eddygrant000@gmail.com',
        'password': 'red@123',
        'balance':20000
    },
    1002:{
        'name': 'Tanuj',
        'age': 25,
        'email': 'tanuj@gmail.com',
        'password': 'tanu123',
        'balance':10000
    }
}
# data = {key: value, key2: value2}
# database.
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

   