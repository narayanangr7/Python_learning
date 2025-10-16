# declaration
userdata = {
    "name":"john", 
    "age":"20",
    "skills":["HTML","CSS","JavaScript"],
    "status": False,
    "comments": {
        "kamalesh":"lorem ipsum",
        "hari":"lorem ipsum"
    }
}

# print(userdata)
print(userdata['name'])
print(userdata['comments'])

# getter
print(userdata.get('status'))

# setter
userdata['email'] = 'johndoe@example.com'
# print(userdata)
userdata['status'] = True
# print(userdata)

# update 
userdata.update({ "age": 25 })
# option 1
userdata['phone'] = None
# option 2
# userdata.update({ "phone" : None })
# print(userdata)

keys = list(userdata.keys())
# print(type(keys))


values = list(userdata.values())
# print(values)



# for i in userdata.keys():
#     print(i)

# for j in userdata.values():
#     print(j)

# for x,y in userdata.items():
#     print(x,y)

# print(userdata.items())


x = {
    "a":1,
    "b":2,
    "c":3
}

print(x.items())

