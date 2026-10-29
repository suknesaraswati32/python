
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr, arr.size, arr.dtype, arr.ndim)

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)



arr = np.array([12, 25, 36, 48, 50, 17, 29, 40, 55, 60])
print(np.max(arr), np.min(arr), np.sum(arr), np.mean(arr))



arr = np.arange(1, 21)
print(arr[arr % 2 == 0])
print(arr[arr % 2 != 0])



arr = np.arange(1, 13)
print(arr.reshape(2, 6))
print(arr.reshape(3, 4))
print(arr.reshape(4, 3))



a = np.arange(1, 10).reshape(3, 3)
b = np.arange(9, 0, -1).reshape(3, 3)
print(a + b)



a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
print(np.matmul(a, b))



arr = np.arange(1, 13).reshape(3, 4)
print(arr.T)



arr = np.arange(1, 17).reshape(4, 4)
print(arr[0])
print(arr[:, -1])
print(np.diag(arr))
print(arr[1:3, :])



arr = np.arange(1, 17).reshape(4, 4)
print(np.sum(arr, axis=1))
print(np.sum(arr, axis=0))



arr = np.arange(1, 21)
print(arr[:5])
print(arr[-5:])
print(arr[::2])
print(arr[::-1])



arr = np.array([10, 60, 25, 75, 40, 90, 15, 55, 30, 80])
arr[arr > 50] = 0
print(arr)



arr = np.array([45, 12, 89, 23, 5, 67, 34])
print(np.sort(arr))
print(np.sort(arr)[::-1])



arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60])
print(np.unique(arr))



a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.hstack((a, b)))
print(np.vstack((a, b)))



marks = np.array([78, 85, 90, 67, 88, 76, 95, 82, 70, 89])
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))

marks = np.array([65, 78, 82, 90, 55, 72, 88, 95, 60, 75,
                  80, 68, 92, 85, 70, 77, 83, 58, 96, 74])
avg = np.mean(marks)
print("Average:", avg)
print(marks[marks > avg])

arr = np.arange(1, 25).reshape(2, 3, 4)
print(arr)
print(arr.ndim, arr.shape, arr.size)

arr = np.arange(1, 25).reshape(2, 3, 4)
print(arr[0, 0, 0])
print(arr[-1, -1, -1])
print(arr[0, 1, 2])
print(arr[1, 2, 3])

arr = np.arange(1, 25).reshape(2, 3, 4)
print(np.sum(arr))
print(np.sum(arr, axis=(1, 2)))
print(np.sum(arr, axis=2))
print(np.sum(arr, axis=1))

arr = np.random.randint(1, 101, size=(2, 3, 4))
print(arr)
arr[arr > 50] = 0
print(arr)

arr = np.random.randint(1, 101, size=(3, 4, 5))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))

arr = np.arange(1, 25).reshape(2, 3, 4)
print(arr)
print(arr.flatten())

arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()
print(flat)
print(np.sum(flat))
print(np.mean(flat))
print(np.max(flat))
print(np.min(flat))

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
print(flat[flat > 50])
print(flat[flat % 2 == 0])
print(flat[flat < np.mean(flat)])
