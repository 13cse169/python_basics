import random

num_1 = random.random()
print(num_1)

num_2 = random.randint(1, 10)
print(num_2)

l1 = ['apple', 'orange', 'banana', 'kiwi']
str_1 = random.choice(l1)
print(str_1)

print(l1)
random.shuffle(l1)
print(l1)