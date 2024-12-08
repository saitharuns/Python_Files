choice=float(input('Options \n1.C to F\n2.F to C\nEnter your choice : '))

if(choice==1):
    cel=float(input("enter the celcius : "))
    print("the Fher : ",(cel*9/5)+32)
elif(choice==2):
    fh=float(input("enter the celcius : "))
    print("the Celcius : ",(fh-32)*5/9)
else:
    print("Invalid Choice")