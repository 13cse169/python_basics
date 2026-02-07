def creation_examples():
	print('--- creation_examples ---')
	a = [1, 2, 3]
	b = list(range(5))
	c = ["a", 1, 2.5, [3, 4]]  # heterogeneous
	print('a =', a)
	print('b =', b)
	print('c =', c)


def indexing_and_slicing():
	print('--- indexing_and_slicing ---')
	a = ['zero', 'one', 'two', 'three', 'four']
	print('a[0] ->', a[0])
	print('a[-1] ->', a[-1])
	print('a[1:4] ->', a[1:4])
	print('a[:3] ->', a[:3])
	print('a[::2] ->', a[::2])


def mutability_and_methods():
	print('--- mutability_and_methods ---')
	a = [1, 2, 3]
	print('original a ->', a)
	a.append(4)
	print('after append(4) ->', a)
	a.extend([5, 6])
	print('after extend([5,6]) ->', a)
	a.insert(0, 0)
	print('after insert(0,0) ->', a)
	popped = a.pop()
	print('pop() ->', popped, ', a ->', a)
	a.remove(0)
	print('after remove(0) ->', a)
	print('index of 3 ->', a.index(3))
	a.reverse()
	print('after reverse ->', a)
	a.sort(reverse=True)
	print('after sort(reverse=True) ->', a)


def list_comprehensions():
	print('--- list_comprehensions ---')
	squares = [x * x for x in range(6)]
	print('squares ->', squares)
	evens = [x for x in range(10) if x % 2 == 0]
	print('evens ->', evens)
	# nested comprehension
	grid = [[i * j for j in range(4)] for i in range(3)]
	print('grid ->', grid)


def nested_lists_and_aliasing():
	print('--- nested_lists_and_aliasing ---')
	# nested lists are references; copying pitfalls
	row = [0] * 3
	matrix_bad = [row] * 3  # shallow repetition
	matrix_bad[0][0] = 99
	print('matrix_bad (shared rows) ->', matrix_bad)

	# correct way to create independent rows
	matrix_good = [[0] * 3 for _ in range(3)]
	matrix_good[0][0] = 7
	print('matrix_good (independent rows) ->', matrix_good)


def conversion_and_unpacking():
	print('--- conversion_and_unpacking ---')
	t = (1, 2, 3)
	l = list(t)
	print('tuple -> list:', l)
	a, b, *rest = [10, 20, 30, 40]
	print('unpacked a,b,rest ->', a, b, rest)


def main():
	creation_examples()
	indexing_and_slicing()
	mutability_and_methods()
	list_comprehensions()
	nested_lists_and_aliasing()
	conversion_and_unpacking()


if __name__ == '__main__':
	main()

