print("BANK LOAN ELIGIBILITY")

age=int(input("enter the age : "))
if(age>18 and age<60):
    income=float(input("enter the income : "))
    if(income>=30000):
        print("you are eligible for loan")
    else:
        cosign=input("have co-signer press yes\nno co-signer press no\n--> ")
        if(cosign=='yes'):
            print("you are eligible for loan")
        elif(cosign=='no'):
            print("you are not eligible for loan")
        else:
            print("invlaid entry")
else:
    print("you are not eligible for loan")

