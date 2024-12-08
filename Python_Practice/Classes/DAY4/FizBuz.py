i=1
while(i<=20):
    if(i%5==0):
        print(i," =Giz")
    elif(i%2==0 and i%3==0):
        print(i," =Fizbuz")
    elif(i%2==0):
        print(i," =Fiz")
    elif(i%3==0):
        print(i," =Buz")
    else:
        print(i)
    i+=1