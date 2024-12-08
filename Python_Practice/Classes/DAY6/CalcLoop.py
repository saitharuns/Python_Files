var1=float(input("enter the number : "))
check = 0
while True:
    try:
        if(check == 0):
            result=var1
            check = 1
            
        symbol=input("enter the symbol : ")
        var2=float(input("enter the number : "))
        
        if(symbol=='+'):
            result=result+var2
        elif(symbol=='-'):
            result=result-var2
            
        elif(symbol=='*'):
            result=var1*var2
            
        elif(symbol=='/'):
            result=var1/var2
            
        elif(symbol=='%'):
            result=var1%var2
            
        else:
            print("invaild input")
        
    except Exception as e:
        print(e)
    finally:
        print(result)