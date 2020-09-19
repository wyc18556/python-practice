def my_print(a, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")


# 指定参数，可以不按照方法定义的顺序传参
my_print(1, c=2, b=3)


# 可变长参数方法，参数前面加上「*」号
def how_long(first, *other):
    return 1 + len(other)


print(how_long(1))
print(how_long(1, 2))
print(how_long(1, 2, 3))

# 函数作用域
var1 = 123


def local():
    var1 = 456
    print(var1)


def global_func():
    # global 关键字修饰后就是全局作用域了
    global var1
    var1 = 456
    print(var1)


local()
print(var1)

global_func()
print(var1)

# 迭代器
myList = [1, 2, 3]
it = iter(myList)
print(next(it))
print(next(it))
print(next(it))


# print(next(it)) exception

# 使用 yield 自定义迭代器
def my_range(start, end, step):
    while start < end:
        yield start
        start += step


for i in my_range(10, 15, 0.5):
    print(i)
