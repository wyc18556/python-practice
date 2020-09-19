try:
    year = int(input("请输入年份："))
except ValueError as e:
    print(f"年份必须是数字：{e}")
finally:
    print("程序结束")