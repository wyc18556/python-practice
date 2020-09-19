import re


# . 代表任意一个字符
# \d 代表数字
# \D 代表非数字
# [n] 代表指定字符 n，可以写多个
# ? 表示匹配 0 个或 1 个
# + 表示匹配 1 个或多个
# * 表示匹配 0 个或多个
# {m} 表示指定匹配 m 个

def match_date(date_str):
    p = re.compile(r'(\d+)-(\d+)-(\d+)')
    result = p.match(date_str)
    year = result.group(1)
    print(year)
    year, month, day = result.groups()
    print(year)
    print(month)
    print(day)


# match 是从开头开始做精确匹配
match_date('2020-9-16')
 

# match_date('abc2020-09-10')  # Exception


def search_date(date_str):
    p = re.compile(r'(\d+)-(\d+)-(\d+)')
    result = p.search(date_str)
    year = result.group(1)
    print(year)
    year, month, day = result.groups()
    print(year)
    print(month)
    print(day)


# search 是逐个匹配
search_date('2020-9-16')
search_date('abc2020-09-10abc2020-09-16')  # Exception

# sub 是匹配并替换
source = '123-456-789 # 这是一段注释'
source_1 = re.sub(r'#.*$', '', source)
print(source_1)
source_2 = re.sub(r'\D+', '', source_1)
print(source_2)

# findall
find = re.findall(r'\d+-\d+-\d+', "abc2020-09-10abc2020-09-16")
print(find)
