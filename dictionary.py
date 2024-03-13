dic = {
    "sush": "tubbi",
    "shiva": "gulmya",
    "nagya": "jutty"
}

print(dic["sush"])
print(dic.get("shiva"))

print(dic)  # {'sush': 'tubbi', 'shiva': 'gulmya', 'nagya': 'jutty'}

print(dic.keys())  # dict_keys(['sush', 'shiva', 'nagya'])

print(dic.values())  # dict_values(['tubbi', 'gulmya', 'jutty'])

print(dic.items())  # dict_items([('sush', 'tubbi'), ('shiva', 'gulmya'), ('nagya', 'jutty')])

print(dic.get("swati"))  # returns "none"

# print(dic["swati"]) #Throws an error


dic2 = {"swati": "kaddi"}
dic.update( dic2 )
print(dic)

dic.pop("swati") # removes specified item
print(dic)

dic.popitem() # removes last added item
print(dic)


