r=int(input("enter the total number of rows : "))
count=1
for var in range(r+1):
    for var2 in range(var):
        print(count,end=' ')
        count+=1
    print('')
