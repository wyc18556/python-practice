from pandas import Series, DataFrame
import pandas as pd

# 通过数组构建 Series
# obj = Series([4, 5.4, 6, -9])
# print(obj)
# print(obj.index)
# print(obj.values)

# # 通过字典构建 Series
# data = {'beijing': 17000, 'shanghai': 15000, 'hangzhou': 14000}
# obj = Series(data)
# print(obj)
# # 修改索引
# obj.index = ['bj', 'sh', 'hz']
# print(obj)

# # 自己指定索引
# obj_1 = Series([3, 5, 7, 1], index=['d', 'r', 'a', 'w'])
# print(obj_1)
# # 通过索引修改数据
# obj_1['r'] = 9
# print(obj_1)
#
# # 判断索引是否存在
# print('q' in obj_1)
# print('d' in obj_1)
