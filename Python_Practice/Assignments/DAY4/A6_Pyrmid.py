rows = int(input("enter the total number of rows"))
for i in range(1, rows+1):
    for j in range(rows - i):# used for creating the space
        print(" ", end="")
    for k in range(1, i+1):
        print(k, end=" ")
    print("")
