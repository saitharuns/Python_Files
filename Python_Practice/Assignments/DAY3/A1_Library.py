print("Book overdue")

due=int(input("enter 1 if the book is Due \nenter 2 if the book has no due\n choice--> "))

if(due==1):
    print("book is due...\n")
    days=int(input("enter the number of due days: "))
    if(days>=1 and days<=5):
        print("fine of 50rs imposed....")
    elif(days>=6 and days<=10):
       print("fine of 100rs imposed...")
    else:
        print("fine of 500rs imposed...")
else:
    print("book is returned on time...")