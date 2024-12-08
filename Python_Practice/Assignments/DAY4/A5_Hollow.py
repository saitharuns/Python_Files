x=int(input("enter the total number of rows : "))
for i in range(1,x+1): 
    for j in range(1,x+1):
        if (i==1 or j==x or i==x or j==1):
            print(j,end=' ')
        else:
            print(end='  ')

    print('')
