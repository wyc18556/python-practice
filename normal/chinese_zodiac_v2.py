# 通过年份计算生肖
chineseZodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# for 循环
for cz in chineseZodiac:
    print(cz)

for i in range(13):
    print(i)

for i in range(1, 13):
    print(i)

for year in range(2000, 2018):
    print(f"{year} 年是{chineseZodiac[year % 12]}年")

# while 循环
year = 2000
while year < 2018:
    if year != 2014:
        print(f"{year} 年是{chineseZodiac[year % 12]}年")
    year += 1
