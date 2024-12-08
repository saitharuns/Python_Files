try:
    num1=int(input("enter the number 1 : "))
    num2=int(input("enter the number 2 : "))
    print(num1/num2)
except ZeroDivisionError:
    print("could not divide by zero")