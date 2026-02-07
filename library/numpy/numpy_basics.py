import numpy as np


def creation_examples():
	# Create arrays from lists
	a = np.array([1, 2, 3, 4, 5])
	b = np.array([[1, 2, 3], [4, 5, 6]])
	print("1D array:", a)
	print("2D array:\n", b)

	# Common creation functions
	zeros = np.zeros((2, 3))
	ones = np.ones((2, 3), dtype=int)
	arange = np.arange(0, 10, 2)
	lin = np.linspace(0, 1, 5)  # 5 values from 0 to 1
	print("zeros:\n", zeros)
	print("ones:\n", ones)
	print("arange:", arange)
	print("linspace:", lin)


def dtype_and_copy():
	x = np.array([1, 2, 3], dtype=np.float64)
	print("dtype:", x.dtype)

	# view vs copy
	y = x.view()
	z = x.copy()
	y[0] = 9.0
	print("after modifying view y -> x:", x)
	z[1] = -1.0
	print("after modifying copy z -> x (unchanged):", x)


def arithmetic_and_ufuncs():
	a = np.array([1, 2, 3])
	b = np.array([4, 5, 6])
	print("a + b:", a + b)
	print("a * b:", a * b)
	print("sin(a):", np.sin(a))
	print("exp(a):", np.exp(a))


def broadcasting_examples():
	A = np.arange(6).reshape(2, 3)
	v = np.array([10, 20, 30])
	print("A:\n", A)
	print("v:", v)
	# v will be broadcast across the rows of A
	print("A + v:\n", A + v)


def indexing_and_slicing():
	a = np.arange(10)
	print("a:", a)
	print("a[2:7:2]:", a[2:7:2])

	M = np.arange(1, 10).reshape(3, 3)
	print("M:\n", M)
	print("M[0, :]:", M[0, :])
	print("M[:, 1]:", M[:, 1])


def reshape_and_transpose():
	x = np.arange(12)
	print("original shape:", x.shape)
	X = x.reshape(3, 4)
	print("reshaped (3,4):\n", X)
	print("transpose:\n", X.T)


def statistics_and_axis():
	X = np.array([[1, 2, 3], [4, 5, 6]])
	print("X:\n", X)
	print("mean (all):", X.mean())
	print("mean axis=0 (columns):", X.mean(axis=0))
	print("mean axis=1 (rows):", X.mean(axis=1))


def random_examples():
	# NumPy's random module (recommended: use Generator in newer code)
	rng = np.random.default_rng(0)  # seed for reproducibility
	print("random integers:", rng.integers(0, 10, size=5))
	print("random normal sample:\n", rng.normal(loc=0.0, scale=1.0, size=(2, 3)))


def main():
	print("--- creation_examples ---")
	creation_examples()
	print("\n--- dtype_and_copy ---")
	dtype_and_copy()
	print("\n--- arithmetic_and_ufuncs ---")
	arithmetic_and_ufuncs()
	print("\n--- broadcasting_examples ---")
	broadcasting_examples()
	print("\n--- indexing_and_slicing ---")
	indexing_and_slicing()
	print("\n--- reshape_and_transpose ---")
	reshape_and_transpose()
	print("\n--- statistics_and_axis ---")
	statistics_and_axis()
	print("\n--- random_examples ---")
	random_examples()


if __name__ == "__main__":
	main()