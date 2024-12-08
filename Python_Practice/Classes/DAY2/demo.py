var1=10
var2=20
#temp=0

#temp=var1 #temp 10
#var1=var2 #var1 20
#var2=temp #var2 10

#var1,var2=var2,var1

#var1=var1+var2 #30
#var2=var1-var2 #10
#var1=var1-var2 #20

print(var1 and var2)
print(var1 or var2)
