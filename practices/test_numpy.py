try:
    import sys
    import numpy as np
except Exception:  # pragma: no cover - environment
    print("NumPy is not installed. Install it with: pip install numpy")
    sys.exit(1)


def creation_examples():

    a = np.array([1, 2, 3, 4, 5])
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print("1D array:", a)
    print("2D array:\n", b)

    zeros = np.zeros((2, 3), dtype=int)
    ones = np.ones((2, 3), dtype=int)
    arange = np.arange(0, 10, 2)
    lin = np.linspace(0, 1, 5)
    print("zeros:\n", zeros)
    print("ones:\n", ones)
    print("arange:", arange)
    print("linspace:", lin)


def dtype_and_copy():

    x = np.array([1, 2, 3], dtype=np.float64)
    print("Original array:", x, x.dtype)

    y = x.view()
    z = x.copy()
    y[0] = 9.0
    print("after modifying view y -> x:", x)
    z[1] = -1.0
    print("after modifying copy z -> x (unchanged):", x)

def arithmetic_and_ufuncs():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("a:", a, "b:", b)
    print("a + b:", a + b)
    print("a * b:", a * b)
    print("sin(a):", np.sin(a))
    print("exp(a):", np.exp(a))

def broadcasting_examples():
    A = np.arange(6).reshape(2, 3)
    V = np.array([10, 20, 30])
    print("A:\n", A)
    print("V:", V)
    print("A + V:\n", A + V)

def indexing_and_slicing():
    a = np.arange(10)
    print("a:", a)
    print("a[2:7:2]:", a[2:7:2])

    M = np.arange(1, 10).reshape(3, 3)
    print("M:\n", M)
    print("M[0, :]:", M[0, :])

def reshape_and_transpose():
    x = np.arange(12)
    print("Original x:", x)
    M = x.reshape(3, 4)
    print("Reshaped M (3x4):\n", M)
    MT = M.T
    print("Transposed MT (4x3):\n", MT)

def statistics_and_axis():
    M = np.array([[1, 2, 3], [4, 5, 6]])
    print("M:\n", M)
    print("Mean of M:", M.mean())
    print("Mean of M along axis 0 (columns):", M.mean(axis=0))
    print("Mean of M along axis 1 (rows):", M.mean(axis=1))

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

if __name__ == "__main__":
    print("Running NumPy basics examples...")
    
    # x = [1, 2, 3]
    # x.append(4)
    # x.append([5, 6])
    # x.extend([7, 8])
    # print(x)
    main()