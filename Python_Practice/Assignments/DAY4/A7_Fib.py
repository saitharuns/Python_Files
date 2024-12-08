value=int(input("enter the number for fibbonacci series : "))
a=0
b=1
for var in range(value):
    print(a, end=" ")
    next= a+b
    a=b
    b=next