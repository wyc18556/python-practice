import numpy as np

# 整型数组
array = np.array([2, 3, 4])
print(array)
print(array.dtype)

# 浮点型数组
array_1 = np.array([1, 2, 3.5])
print(array_1.dtype)

# 数组相加
print(array + array_1)

# 对数组进行计算会对数组内元素依次操作
print(array_1 * 10)
print(array_1 + 1.5)

# 二维数组
data = [1, 2, 3], [4, 5, 6]
two_dimensional_array = np.array(data)
print(two_dimensional_array)

# 定义矩阵，并初始化数据为 0
two_dimensional_array_zero = np.zeros((3, 5))
print(two_dimensional_array_zero)

# 定义矩阵，并初始化数据为 1
two_dimensional_array_one = np.ones((3, 5))
print(two_dimensional_array_one)

# 定义矩阵，并初始化数据为空，会设置随机数
two_dimensional_array_empty = np.empty((3, 5, 2))
print(two_dimensional_array_empty)

# 切片操作
array = np.arange(10)
print(array)
print(array[4])

# array[4:6] = 10
# print(array)

array_slice = array[4:6].copy()
array_slice[:] = 15
print(array_slice)
print(array)

