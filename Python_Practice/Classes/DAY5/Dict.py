var={
    #keys  :   #values
    'name':'sai',
    'DOB':'21-12-2001',
    'Place':'Bangarapet'
}

print(var)
print(type(var))

#to get a particular values in dictonary
print(var.get("name"))

#prints the keys that are available in the dict
print(var.keys())

#prints the values that are available in the dict
print(var.values())

#prints the item which as both keys and values
print(var.items())

#updating the values in the dict
var.update({"Place":"KGF"})
print(var)

#delete the particular key
var.pop('name')
print(var)

#empty the dict
var.clear()
print(var)

keys=['name','age','gender']
values=['sai','23','male']
data=dict(zip(keys,values))
print(data)