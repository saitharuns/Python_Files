var="Sai Tharun From Bangarapet"

print(len(var))

#slicing in string
print(var[0:3])
print(var[:4])
print(var[8:])
#negative index starts from the end
print(var[-1])
print(var[-9:-1])

#upper and lower case
print(var.upper())
print(var.lower())

var1="                      Sai       tharun    "

#strip is used to remove the extra spaces 
print(var1.strip())

#replacing the particular word
print(var1.replace('Sai','Tharun'))

var="sai,tharun / is from / bangarapet"
#splitting the words based on the sta3tement we require
print(var.split(" "))
print(var.split("/"))
print(var.split(","))

#checking the conditions like alphanumeric, numeric, alphabet
password="A123B "
print(password.isdigit())#check digit
print(password.isalnum())#check alphanumeric
print(password.isalpha())#checks only alphabet
print(password.isspace())#checks space
print(password.isupper())#checks upper case
print(password.islower())#checks lower case

var=[1,2,3,9,4,6,8,10]
result=sorted(var)
print(result)

result=sorted(var,reverse=True)
print(result)



var=[1,2,3,9,4,6,8,10]
var.sort()
print(var)
#for descending
var.sort(reverse=True)
print(var)