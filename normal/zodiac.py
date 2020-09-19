# 定义一个元组
tuples = (4, 5, 3, 1, 7)
targetTuple = 4
# 过滤函数进行过滤操作
filterList = list(filter(lambda x: x <= targetTuple, tuples))
# 过滤后结果
print(type(filterList))
print(filterList)
print(len(filterList))

# 计算星座
zodiacName = ("摩羯座", "水瓶座", "双鱼座", "白羊座",
              "金牛座", "双子座", "巨蟹座", "狮子座",
              "处女座", "天秤座", "天蝎座", "射手座")

zodiacDays = ((1, 20), (2, 19), (3, 21), (4, 21),
              (5, 21), (6, 22), (7, 23), (8, 23),
              (9, 23), (10, 23), (11, 23), (12, 23))

birthday = (8, 14)
zodiacDayFilterResult = filter(lambda x: x <= birthday, zodiacDays)
zodiacDayLength = len(list(zodiacDayFilterResult))
print(zodiacName[zodiacDayLength % 12])
