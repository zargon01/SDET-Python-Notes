import json

with open("j.json","r") as f: # read mode
    data = json.load(f)       #Load data
print(data)

x = {
    "name":"Shivam",
    "age" : 10
}

with open("j.json","a") as f: #append mode
    data = json.dump(x, f, indent = 4)  #Dump data
print(data)

with open("j.json","w") as f: #clear previous data and write
    data = json.load(f)
print(data)