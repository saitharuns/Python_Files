print("Welcome To TONI's BANK")

print("insert your card")

pin=int(input("enter the six digit pin"))

bal=100000
if(pin==123456):

    opt=int(input("enter the the options \n1.Deposit\n2.Withdraw\n3.Balance enquiry\n -->"))

    if(opt==1):
        print("_______Deposit___________")
        amt=float(input("enter the amount inserted"))
        if(amt>50000):
            print("amount is exceeded!!! ")
        elif(amt<100):
            print("deposit the minimum amount ")
        else:
            print("amount is depositied successfully!!!! ")
            opt1=int(input("enter 1 to show balance "))
            if(opt1==1):
                print("the available balance is : ",bal+amt)
                print("thank you visit again....")
            else:
                print("thank you visit again....")
    elif(opt==2):
        print("_______Withdraw___________")
        amt=float(input("enter the amount "))
        if(amt>15000):
            print("mamount cannot be more than 15000 ")
        elif(amt<100):
            print("enter the amount more than 100 ")
        else:
            print("amount is withdrawn successfully !!!! ")
            opt1=int(input("enter 1 to show balance "))
            if(opt1==1):
                print("the available balance is : ",bal-amt)
                print("thank you visit again....")
            else:
                print("thank you visit again....")
    elif(opt==3):
        print("________Balance Info___________")
        print("available balance: ",bal)
    else:
        print("try again.......")
else:
    print("invalid pin.....")