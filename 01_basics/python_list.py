myList = ['apple', 'orange', 'banana', 'kiwi']
print("-----------------------------------------")

print(myList)
print(myList[-1])
print(myList[2:3])
print(myList[1:1])

print("-----------------------------------------")

myList[3] = "White"
print(myList)

myList[1:2] = "Green"
print(myList)

print("-----------------------------------------")

myList = ['apple', 'orange', 'banana', 'kiwi']

myList[1:2] = ["Green"]
print(myList)

myList[1:1] = ["Lemon", "Lemon"]
print(myList)

print(myList[1:3])

myList[1:3] = []
print(myList)

print("-----------------------------------------")

for fruit in myList:
    print(fruit)

for fruit in myList:
    print(fruit, end="-")

print()

print("-----------------------------------------")

if "Grapes" in myList:
    print("Yes")

myList.append("Grapes")

if "Grapes" in myList:
    print("Yes")

print("-----------------------------------------")

print(myList)
print(myList.pop())
print(myList)
myList.remove("Green")
print(myList)

print("-----------------------------------------")

print(myList)

myList.insert(1, "Grapes")

print(myList)

print("-----------------------------------------")

myListCopy = myList
print(myListCopy)

myListCopy.insert(2, "Lemon")
print(myListCopy)
print(myList)

print("-----------------------------------------")

myListCopy_2 = myList.copy()
print(myListCopy_2)

myListCopy_2.insert(2, "Mango")
print(myListCopy_2)
print(myList)

print("-----------------------------------------")

numList_1 = [x**2 for x in range(10)]
print(numList_1)

numList_2 = [x**3 for x in range(5)]
print(numList_2)

print("-----------------------------------------")