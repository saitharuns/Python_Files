file=open("NewText.txt",mode='r')

#converts the string to the list datatype 
var1=file.readlines(30)

#uisng the index of the list the particular line
print(var1[2])
file.close()