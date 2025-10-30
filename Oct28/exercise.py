import json

data= '{"name":"Narayanan","age":17,"isStudent":True,"Skils":["Pythin","SQL","java script",],"address":{"City":"Mumbai","pincode": 400001}}'

list_of_data = json.loads(data)

print(list_of_data)