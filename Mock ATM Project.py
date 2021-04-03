from datetime import datetime

now = datetime.now()
 
print(now)
print("Welcome")
name = input ("What is your name? \n")
allowedUsers = ['Jujubee','Bianca','Tia']
allowedPassword = ['passwordJujubee','passwordBianca','passwordTia']
balance = [100, 200, 300]
selectedOption = 1

if (name in allowedUsers):
    password = input ("What is your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
       while 0 < selectedOption <= 3:
        print('Welcome %s' % name)
        print('These are the avaialble options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        selectedOption = int(input('Please select an option: '))

        if(selectedOption == 1):
                print('you selected %s' % selectedOption)
                cash = input ('How much would you like to withdraw? \n')
                print('take your cash')
                print ('\n')

        elif(selectedOption == 2):
                print('you selected %s' % selectedOption)
                deposit = int(input ('How much would you like to deposit? \n'))
                currentBalance = balance[userId]
                newBalance = currentBalance + deposit
                print ('The current balance is $ %d ' % newBalance )
                print ('\n')

        elif(selectedOption ==3):
                print('you selected %s' % selectedOption)
                complaint = input("What issue would you like to report? \n")
                print ("Thank you for contacting us")
                print ('\n')
            
        else: 
                print('Invalid Option selected, please try again')
    else:
        print('Password Incorrect, please try again')

else:
    print ("Name not found, please try again")




