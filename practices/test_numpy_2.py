import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

minimum = np.min(arr)
maximum = np.max(arr)
mean = np.mean(arr)
median = np.median(arr)
mode = np.bincount(arr).argmax()

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

arr[arr > 30] = 0
print("Modified Array (values > 30 set to 0):", arr)

arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = np.where(arr > 30, 99, arr)
print("New Array (values > 30 set to 0 using np.where):", arr, new_arr)

#Find indices where value > 50
arr = np.array([10, 20, 30, 40, 50, 60])
result = np.where(arr < 50)
print(result)

#Find sum of all elements
arr = np.array([10, 20, 30, 40])
arr_sum = np.sum(arr)
print(arr_sum)

#Find row-wise sum
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr)
row_sum = np.sum(arr, axis=1)
print(row_sum)

#Find column-wise mean
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr)
col_mean = np.mean(arr, axis=0)
print(col_mean)

#Find cumulative sum
arr = np.array([1, 2, 3, 4])
cumulative_sum = np.cumsum(arr)
print(cumulative_sum)

#Convert 1D array to 2D array
arr_2d = arr.reshape(2, 2)
print(arr_2d)