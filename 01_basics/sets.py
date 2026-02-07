def creation_and_membership():
	print('--- creation_and_membership ---')
	s = {1, 2, 3, 4}
	s2 = set([3, 4, 5, 6])
	empty = set()
	print('s ->', s)
	print('s2 ->', s2)
	print('empty ->', empty)
	print('3 in s ->', 3 in s)
	print('10 in s ->', 10 in s)


def basic_set_operations():
	print('--- basic_set_operations ---')
	a = {1, 2, 3, 4}
	b = {3, 4, 5, 6}
	print('a:', a)
	print('b:', b)
	print('union a | b ->', a | b)
	print('intersection a & b ->', a & b)
	print('difference a - b ->', a - b)
	print('symmetric_difference a ^ b ->', a ^ b)


def methods_and_mutation():
	print('--- methods_and_mutation ---')
	s = {1, 2, 3}
	print('start s ->', s)
	s.add(4)
	print('after add(4) ->', s)
	s.update([5, 6])
	print('after update([5,6]) ->', s)
	s.discard(10)  # no error if missing
	print('after discard(10) ->', s)
	# remove will raise if element missing
	try:
		s.remove(100)
	except KeyError:
		print('remove(100) raised KeyError (as expected)')
	popped = s.pop()
	print('pop() ->', popped, ', s now ->', s)
	s.clear()
	print('after clear() ->', s)


def frozenset_and_hashability():
	print('--- frozenset_and_hashability ---')
	s = {1, 2, 3}
	fs = frozenset(s)
	print('frozenset(fs) ->', fs)
	# frozenset is hashable and can be used as a dict key
	d = {fs: 'immutable set key'}
	print('dict with frozenset key ->', d)


def set_comprehensions_and_dedup():
	print('--- set_comprehensions_and_dedup ---')
	squares = {x * x for x in range(6)}
	print('squares ->', squares)
	# deduplicate a list while preserving iteration into a set (order not preserved)
	data = [1, 2, 2, 3, 4, 4, 5]
	deduped = set(data)
	print('data ->', data)
	print('deduped (set) ->', deduped)


def pitfalls_and_notes():
	print('--- pitfalls_and_notes ---')
	# sets require hashable elements
	try:
		s = set()
		s.add([1, 2])  # list is unhashable
	except TypeError as e:
		print('adding unhashable element raised TypeError (as expected):', e)

	print('sets are unordered: iteration order may vary ->', {3, 1, 2})


def main():
	creation_and_membership()
	basic_set_operations()
	methods_and_mutation()
	frozenset_and_hashability()
	set_comprehensions_and_dedup()
	pitfalls_and_notes()


if __name__ == '__main__':
	main()
