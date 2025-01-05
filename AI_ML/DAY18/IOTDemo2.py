from ubidots import ApiClient

API = ApiClient(token='BBUS-JSY2bdVX8rf0jgKJJu7Ad2uqJEj2fj',apikey='BBUS-c00406df8683da55737c4e54b19623ca5af')
var=API.get_variable(var_id='6763cd51d79ffe37830cbb20')
var2=API.get_variable(var_id="6763dc12a7ec7b3dec477a30")

while True:
    val=input("enter the value:")
    var.save_value({'value':val})

    val2=input("enter the value of temp :")
    var2.save_value({'value':val2})
    
    cont=input("1 to cont 0 to stop : ")
    if cont==0:
        break