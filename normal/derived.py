# 求 1 到 10 所有偶数的平方
aList = []
for i in range(1, 11):
    if i & 1 == 0:
        aList.append(i * i)
print(aList)

# 列表推导式
bList = [i * i for i in range(1, 11) if i & 1 == 0]
print(bList)

# 课程列表转字典
classList = ["语文课", "数学课", "物理课"]
classDict_1 = {}
for i in range(len(classList)):
    classDict_1[classList[i]] = 0
print(classDict_1)

# 字典推导式
classDict_2 = {classList[i]: 0 for i in range(len(classList))}
print(classDict_2)
