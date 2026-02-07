def creation_and_immutability():
	print('--- creation_and_immutability ---')
	t = (1, 2, 3)
	print('t =', t)
	# tuples are immutable; the following would raise an error if uncommented
	# t[0] = 10
	print('len(t) =', len(t))


def single_element_and_empty():
	print('--- single_element_and_empty ---')
	single = (42,)
	not_a_tuple = (42)
	empty = ()
	print('single (with comma) ->', single, 'type:', type(single))
	print('not_a_tuple (no comma) ->', not_a_tuple, 'type:', type(not_a_tuple))
	print('empty tuple ->', empty)


def unpacking_and_swap():
	print('--- unpacking_and_swap ---')
	t = ('Alice', 30, 'Engineer')
	name, age, role = t
	print('name, age, role ->', name, age, role)

	# swap two variables using tuple unpacking
	a, b = 1, 2
	print('before swap a,b ->', a, b)
	a, b = b, a
	print('after swap a,b ->', a, b)


def tuples_as_dict_keys_and_nested():
	print('--- tuples_as_dict_keys_and_nested ---')
	# tuples are hashable when they contain only hashable elements
	d = {}
	d[(0, 0)] = 'origin'
	d[(1, 2)] = 'point'
	print('dict with tuple keys ->', d)

	nested = ((1, 2), (3, 4))
	print('nested tuple ->', nested)


def count_and_index_methods():
	print('--- count_and_index_methods ---')
	t = (1, 2, 2, 3, 2)
	print('t ->', t)
	print('t.count(2) ->', t.count(2))
	print('t.index(3) ->', t.index(3))


def namedtuple_note():
	print('--- namedtuple_note ---')
	from collections import namedtuple

	Point = namedtuple('Point', ['x', 'y'])
	p = Point(1, 2)
	print('namedtuple Point ->', p, 'access by name p.x ->', p.x)


def main():
	creation_and_immutability()
	single_element_and_empty()
	unpacking_and_swap()
	tuples_as_dict_keys_and_nested()
	count_and_index_methods()
	namedtuple_note()


if __name__ == '__main__':
	main()

