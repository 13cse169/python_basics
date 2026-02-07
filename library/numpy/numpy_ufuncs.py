import numpy as np


def basic_elementwise():
	print("--- basic_elementwise ---")
	a = np.array([1, 2, 3, 4])
	b = np.array([10, 20, 30, 40])
	print("a:", a)
	print("b:", b)

	# Common ufuncs operate elementwise and are fast (C-implemented)
	print("add:", np.add(a, b))
	print("multiply:", np.multiply(a, b))
	print("maximum:", np.maximum(a, b))
	print("power a**2:", np.power(a, 2))

	# ufuncs support an out= parameter to write into pre-allocated arrays
	out = np.empty_like(a)
	np.add(a, b, out=out)
	print("add with out parameter:", out)


def ufunc_methods():
	print("--- ufunc_methods (reduce / accumulate / reduceat) ---")
	a = np.arange(1, 9)  # 1..8
	print("a:", a)

	# reduce applies the ufunc cumulatively and returns a scalar
	print("add.reduce -> sum:", np.add.reduce(a))

	# accumulate returns all intermediate results
	print("add.accumulate:", np.add.accumulate(a))

	# reduceat can compute reductions at specified indices (useful for grouped ops)
	idx = [0, 3, 5]
	print("add.reduceat with indices [0,3,5]:", np.add.reduceat(a, idx))


def outer_and_broadcasting():
	print("--- outer_and_broadcasting ---")
	x = np.array([1, 2, 3])
	y = np.array([10, 20])
	print("x:", x)
	print("y:", y)

	# outer applies a ufunc between all pairs (result shape = (len(x), len(y)))
	print("multiply.outer(x, y):\n", np.multiply.outer(x, y))

	# broadcasting example: x[:, None] broadcasts with y
	print("broadcast via reshape:\n", x[:, None] * y)


def boolean_ufuncs_and_where():
	print("--- boolean_ufuncs_and_where ---")
	a = np.array([1, 2, 3, 4, 5])
	cond = a % 2 == 0
	print("a:", a)
	print("even mask:", cond)

	# use where to select elements
	selected = np.where(cond, a * 10, -a)
	print("where(cond, a*10, -a):", selected)

	# boolean ufuncs like logical_and / logical_or
	b = np.array([5, 4, 3, 2, 1])
	print("logical_and(a>2, b<4):", np.logical_and(a > 2, b < 4))


def vectorize_note():
	print("--- vectorize_note ---")

	def myfunc(x):
		# pure python function: slower than ufuncs, but vectorize provides convenience
		return x * x + 1

	v = np.vectorize(myfunc)
	arr = np.arange(6)
	print("arr:", arr)
	print("vectorized myfunc(arr):", v(arr))
	print("Note: np.vectorize is a convenience wrapper, not a performance tool. For speed, use ufuncs or numba.")


def dtype_and_casting():
	print("--- dtype_and_casting ---")
	a = np.array([1, 2, 3], dtype=np.int32)
	print("a dtype:", a.dtype)
	# ufuncs will upcast when needed
	b = np.array([0.1, 0.2, 0.3], dtype=np.float64)
	print("add int32 + float64 -> dtype:", (np.add(a, b)).dtype)


def main():
	basic_elementwise()
	ufunc_methods()
	outer_and_broadcasting()
	boolean_ufuncs_and_where()
	vectorize_note()
	dtype_and_casting()


if __name__ == "__main__":
	main()

