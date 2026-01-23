str_1 = "Birendra Singh"
str_1_1 = "Birendra Singh Singh Singh"
print("-----------------------------------------")

print(str_1.lower())
print(str_1.upper())
print(str_1)

print(len(str_1))

print(str_1.find("Singh"))
print(str_1.find("singh"))

print(str_1_1.count("Singh"))

print("-----------------------------------------")

f_str = str_1[0]
print(f_str)

slice_str = str_1[0:8]
print(slice_str)

print("-----------------------------------------")

str_2 = "    Birendra Singh     "
print(str_2)
print(str_2.strip())

print("-----------------------------------------")

num_list = "0123456789"
print(num_list)
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])

print("-----------------------------------------")

str_3 = "apple, orange, banana, kiwi"

print(str_3)
print(str_3.split())
print(str_3.split(", "))

print("-----------------------------------------")

chai_type = "Masala"
quantity = 2

order = "I ordered {} cup of {} chai."

print(order)
print(order.format(quantity, chai_type))

print("-----------------------------------------")

fruits = ['apple', 'orange', 'banana', 'kiwi']

print(fruits)
print(" ".join(fruits))
print(", ".join(fruits))

print("-----------------------------------------")

print(str_1)

for letter in str_1:
    print(letter)

str_4 = "Birendra\nSingh"
print(str_4)

str_4 = r"Birendra\nSingh"
print(str_4)

print("-----------------------------------------")