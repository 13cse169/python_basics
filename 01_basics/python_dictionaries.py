myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("-------------------- Access Dictionary Items ---------------------")

print(myDict)

print(myDict["brand"])
print(myDict.get("model"))

print(myDict.keys())
print(myDict.values())

print("-----------------------------------------")

myDict["year"] = 2026
print(myDict)

myDict.update({"year": 2030})
print(myDict)

print("-----------------------------------------")

for data in myDict:
    print(data)

for key, value in myDict.items():
    print(key, value)


print("-----------------------------------------")

print(myDict.pop("year"))
print(myDict)

myDict.update({"color": "Red"})
print(myDict)

myDict.popitem()
print(myDict)

del myDict["model"]
print(myDict)

print("-----------------------------------------")

myDict["model"] = "Mustang"
myDict["year"] = 2026
myDict["color"] = "Red"

myDict_copy = myDict.copy()
print(myDict_copy)

myDict_copy.clear()
print(myDict_copy)
print(myDict)

print("-----------------------------------------")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

print(myfamily["child2"]["name"])

print("-----------------------------------------")