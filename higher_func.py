import time


# 闭包，函数从返回变量变成了函数
def a_line(a, b):
    def line(x):
        return a * x + b

    return line


line1 = a_line(3, 5)
print(line1(10))
print(line1(15))
print(line1(20))


# 无参数简单装饰器
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"函数运行了{end - start}秒")

    return wrapper


@timer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()


# 有参数装饰器
def new_tips(args):
    def tips(func):
        def wrapper(a, b):
            print(f"begin {args} {func.__name__}")
            func(a, b)
            print("end")

        return wrapper

    return tips


@new_tips(args="add_model")
def add(a, b):
    print(a + b)


@new_tips(args="sub_model")
def sub(a, b):
    print(a - b)


add(10, 5)
sub(10, 5)
