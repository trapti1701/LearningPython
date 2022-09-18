# withdrawl
# deposite
# balance
# enter pin

print('welcome to Axis bank')
print('insert your card')
pin=1234
attempt = 3
balance = 1000
while (attempt>0):
    a = int(input('enter your pin to proceed further'))
    if a==pin and attempt>0:
        b= input("please select the operation:\nwithdrawl:\ndeposite:\nbalance check: \n")

        if b == 'withdrawl' :
            print('please enter the amount')
            w = int(input())

            if w <=balance :
                print('please collect your money')
                print('balance:', balance- w)
                print('please collect your card')
                break

            else :
                print('insuficient funds')
                break

        elif b== "deposite":
            print('please enter the amount')
            d = int(input())
            print('please put your money in deposite chamber')
            print('deposite successful, account balance:', balance + d)
            print('please collect your card')
            break

        elif b== "balance check" :
            print ('account balance :', balance)
            break

        else :
            print("You have not selected any option, please try again")
            break

    else :
        print("incorrect pin\n",'you have', attempt-1, "attempts pending")
        attempt = attempt - 1
        continue
