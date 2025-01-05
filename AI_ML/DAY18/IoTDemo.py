from ubidots import ApiClient

API = ApiClient(token='BBUS-JSY2bdVX8rf0jgKJJu7Ad2uqJEj2fj',apikey='BBUS-c00406df8683da55737c4e54b19623ca5af')
var=API.get_variable(var_id='6763cd51d79ffe37830cbb20')
var2=API.get_variable(var_id="6763dc12a7ec7b3dec477a30")

while True:
    last_val=var2.get_values([{3}])
    print(last_val)
    

    
