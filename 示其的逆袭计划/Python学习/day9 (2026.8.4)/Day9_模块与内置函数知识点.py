# Day 9 · 模块与包、常用内置函数 知识点速查 (2026.8.4)
# ============================================
# 今天学会把代码拆到多个文件里，以及 Python 自带的常用工具。
#


# ============================================================
# 一、什么是模块
# ============================================================
# 模块 = 一个 .py 文件
# 把功能拆到不同的 .py 文件里，用 import 导入使用

# 比如你有一个 math_tools.py 文件：
#   def add(a, b): return a + b
#   def multiply(a, b): return a * b

# 在另一个文件里导入：
import math_tools                      # 导入整个模块
math_tools.add(3, 5)                   # 用 模块名.函数名 调用 → 8
math_tools.multiply(3, 5)              # 15

# 【补充】模块文件必须和导入它的文件在同一文件夹吗？
#   不一定，但同一文件夹最简单。Python 按顺序搜索：
#   1. 当前文件所在目录  2. PYTHONPATH  3. 标准库  4. site-packages
#   子文件夹：from tools import utils
#   其他位置：需要 sys.path.append("路径") 加入搜索路径

# 【补充】想查看模块信息：
#   dir(模块)        → 列出所有函数
#   help(模块)       → 完整文档
#   模块.__file__    → 文件路径（math 是 .pyd 编译文件，不是文本）

from math_tools import add             # 只导入某个函数
add(3, 5)                              # 直接用函数名 → 8

from math_tools import add, multiply   # 导入多个
from math_tools import *               # 导入全部（不推荐，容易重名）


# ============================================================
# 二、Python 标准库（自带模块）
# ============================================================
# Python 安装时自带很多模块，不需要 pip 安装，直接 import

# math — 数学函数
import math
math.sqrt(16)            # 4.0         开平方
math.pi                  # 3.14159...  圆周率
math.floor(3.7)          # 3           向下取整
math.ceil(3.2)           # 4           向上取整
math.pow(2, 10)          # 1024.0      幂运算
math.fabs(-5)            # 5.0         绝对值

# random — 随机数
import random
random.random()          # 0~1 之间的随机小数
random.randint(1, 100)   # 1~100 之间的随机整数
random.choice(["a", "b", "c"])   # 随机选一个
random.shuffle(lst)      # 打乱列表（修改原列表）

# os — 操作系统相关
import os
os.getcwd()              # 当前工作目录
os.listdir(".")          # 列出目录下的文件
os.path.exists("data.txt")  # 文件是否存在
os.path.join("a", "b")   # "a/b"  拼接路径（跨平台安全）

# sys — 系统信息
import sys
sys.version              # Python 版本号
sys.exit(0)              # 退出程序


# ============================================================
# 三、常用内置函数（不需要 import，直接可用）
# ============================================================

# 类型转换
int("123")               # 123
float("3.14")            # 3.14
str(123)                 # "123"
list("abc")              # ["a", "b", "c"]
tuple([1, 2])            # (1, 2)
set([1, 1, 2])           # {1, 2}

# 数学类
abs(-5)                  # 5      绝对值
round(3.14159, 2)        # 3.14   四舍五入
max([3, 7, 2])           # 7
min([3, 7, 2])           # 2
sum([1, 2, 3])           # 6
len("hello")             # 5

# 判断类
isinstance(3, int)       # True   判断类型
type(3)                  # <class "int">
bool(0)                  # False
bool("")                 # False
bool([1])                # True

# 迭代类
range(5)                 # 0 1 2 3 4
enumerate(["a", "b"])    # (0,"a") (1,"b")
zip([1, 2], ["a", "b"])  # (1,"a") (2,"b")
sorted([3, 1, 2])        # [1, 2, 3]
reversed([1, 2, 3])      # 反向迭代器

# 输入输出
print("hello")           # 输出
input("请输入：")         # 等待用户输入，返回字符串


# ============================================================
# 四、if __name__ == "__main__"（重点）
# ============================================================
# 当你把函数写在模块里，别人 import 你的模块时，
# 模块里的"测试代码"也会被执行！这很烦人。

# 解决方法：把测试代码放在 if __name__ == "__main__": 里面

# 例子：math_tools.py
# def add(a, b):
#     return a + b
#
# if __name__ == "__main__":
#     # 只有直接运行这个文件时才执行
#     print(add(3, 5))     # 测试代码

# 直接运行：python math_tools.py → 会打印 8
# 被别人 import：不会执行测试代码，只导入函数

# 原理：
# 直接运行时，Python 把 __name__ 设为 "__main__"
# 被 import 时，__name__ 设为模块名（如 "math_tools"）


# ============================================================
# 五、创建自己的模块（实操）
# ============================================================
# 1. 新建一个文件 utils.py：
#   def get_avg(scores):
#       return sum(scores) / len(scores)
#
#   def get_grade(score):
#       if score >= 90: return "优秀"
#       if score >= 80: return "良好"
#       if score >= 60: return "及格"
#       return "不及格"
#
# 2. 在另一个文件里导入：
#   import utils
#   utils.get_avg([95, 87, 92])    # 91.333...
#   utils.get_grade(95)            # "优秀"


# ============================================================
# 六、包（Package）
# ============================================================
# 包 = 文件夹里放多个模块（.py 文件），方便组织代码
# 文件夹里通常有一个 __init__.py（Python 3.3+ 可省略）

# 结构示例：
# mypackage/
# ├── __init__.py
# ├── tools.py
# └── data.py
#
# 导入方式：
# import mypackage.tools
# from mypackage import tools
# from mypackage.tools import some_function


# ============================================================
# 七、第三方库的安装（了解）
# ============================================================
# Python 标准库之外还有海量第三方库，用 pip 安装
# 在终端执行：
#   pip install requests       # 爬虫用
#   pip install numpy          # 数模用（Day 14 会学）
#   pip install pandas         # 数据处理
#   pip install matplotlib     # 画图

# 使用方式和其他模块一样：
# import requests
# import numpy as np           # 常用别名
# import pandas as pd
# import matplotlib.pyplot as plt


# ============================================================
# 八、常用实践：模块化组织你的代码
# ============================================================
# 好的习惯：把通用函数放到单独的 utils.py 里
# 主程序只负责"调用逻辑"，不塞一堆函数定义

# 项目结构示例：
# 项目/
# ├── utils.py          # 通用工具函数
# ├── main.py           # 主程序
# └── data/             # 数据文件夹

# utils.py 里：
# def read_csv(filename): ...
# def get_avg(scores): ...
# def save_result(filename, data): ...

# main.py 里：
# import utils
# data = utils.read_csv("data.csv")
# avg = utils.get_avg(data["scores"])
# utils.save_result("result.txt", avg)


# ============================================================
# 九、常见陷阱
# ============================================================

# 陷阱 1：模块名和变量名重复
# import math
# math = 10        # ❌ 把模块覆盖了，之后 math.sqrt 会报错

# 陷阱 2：from 导入过多导致命名冲突
# from math import *
# from random import *    # 两个模块可能有同名函数，后导入的覆盖前面的

# 陷阱 3：自己的文件名和标准库重名
# 比如你建一个 random.py，会覆盖标准库 random
# 不要用 math.py / random.py / os.py 等标准库名作为文件名

# 陷阱 4：import 的模块路径
# 要 import 自己写的模块，模块文件要和当前文件在同一目录
# 或者放在 sys.path 包含的目录里
