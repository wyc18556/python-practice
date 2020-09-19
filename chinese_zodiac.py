# 通过年份计算生肖
chineseZodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# 按下标访问单个元素
print(chineseZodiac[0])

# 按下标截取
print(chineseZodiac[2:6])

# 倒序访问
print(chineseZodiac[-1])
print(chineseZodiac[-3:-1])

# 按年份计算
year = 2018
print(chineseZodiac[year % 12])

# 判断序列中是否包含某个元素
print("猫" in chineseZodiac)
print("猫" not in chineseZodiac)

# 序列连接操作符
print("猫不在[" + chineseZodiac + "]中")

# 序列重复操作符
print(chineseZodiac * 3)
