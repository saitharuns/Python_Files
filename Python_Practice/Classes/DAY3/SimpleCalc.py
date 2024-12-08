var1=float(input("enter the first number : "))
symbol=input("enter the symbol : ")
var2=float(input("enter the second number : "))


if(symbol=='+'):
    print(var1+var2)
elif(symbol=='-'):
    print(var1-var2)
elif(symbol=='*'):
    print(var1*var2)
elif(symbol=='/'):
    print(var1/var2)
elif(symbol=='%'):
    print(var1%var2)
else:
    print("invaild input")
