word=input("enter the word : ")
count=0
i=0
for var in word:
    i=i+1
    if(var=='a'or var=='e'or var=='i'or var=='o'or var=='u'
       or var=='A'or var=='E'or var=='I'or var=='O'or var=='U'):
        count+=1
        

print(count)