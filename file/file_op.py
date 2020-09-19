# 写入文件
taskWriteFile = open("task.txt", "w")
taskWriteFile.write("1.学习 python 基础语法")
taskWriteFile.close()

# 读取文件
taskReadFile = open("task.txt")
print(taskReadFile.read())
print("---------------")
taskReadFile.close()

# 追加文件
taskWriteFile = open("task.txt", "a")
taskWriteFile.write("\n2.练习操作")
taskWriteFile.close()

# 再次读取文件
taskReadFile = open("task.txt")
print(taskReadFile.read())
print("---------------")
taskReadFile.close()

# 按行读取
taskReadFile = open("task.txt")
print(taskReadFile.readline())
print("---------------")
taskReadFile.close()

taskReadFile = open("task.txt")
lines = taskReadFile.readlines()
for line in lines:
    print(line)
print("---------------")
taskReadFile.close()

# 文件指针操作
taskReadFile = open("seek.txt")
print(taskReadFile.read(1))
taskReadFile.seek(0)
print(taskReadFile.read(4))
# seek 第二个参数代表偏移的位置，0：从文件开头偏移、1：从当前位置偏移、2：从文件结尾偏移
taskReadFile.seek(0, 1)
print(taskReadFile.read(1))

taskReadFile.close()

