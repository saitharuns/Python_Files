def inputvar():
    global num1,num2
    num1=10
    num2=20
    
inputvar()

print(num1+num2)
num1=20
inputvar()
print(num1)