import os
from pathlib import Path

print(os.path.abspath(''))
print(os.path.exists('/Users'))
print(os.path.isdir('/Users'))

p = Path('.')
# 获得当前目录路径
print(p.resolve())

# 指定路径
p = Path('/Users/wyc1856/Documents/a/b/c/d')
if not p.exists():
    p.mkdir(parents=True)
    p = p.joinpath('e.md')
    print(p)
    p.touch()
else:
    print("不是目录")
