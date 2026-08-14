# Day 19 · 装饰器入门 知识点速查 (2026.8.14)
# ============================================
# 今天搞懂：装饰器原理、@ 语法、functools.wraps、计时/日志装饰器。
# 昨天学的闭包是今天的地基：装饰器本质就是"接收函数、返回函数"的闭包。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。


# ============================================================
# 一、为什么需要装饰器
# ============================================================
# 场景：函数已经写好了，现在想给它加"计时、日志、权限检查"等能力，
# 又不想去改函数内部的代码。
# 装饰器 = 给函数"穿外套"，不改原函数，就能增加新功能。

# 目标函数：一个普普通通的加法函数
def add(a, b):
    return a + b

# 想给它加"计时"，普通人会写一个包装函数：
import time

def add_with_time(a, b):
    start = time.perf_counter()
    result = add(a, b)          # 里面还是调用 add
    end = time.perf_counter()
    print(f"耗时：{end - start:.6f} 秒")
    return result

print(add_with_time(3, 4))
# 输出：
# 耗时：0.000xxx 秒
# 7

# 问题来了：如果还有 10 个函数都要计时，就要写 10 个"包装函数"。
# 装饰器能把这个"穿外套"的动作做成模板，一行 @ 就套上。


# ============================================================
# 二、复习：函数是"一等对象"
# ============================================================
# 函数名不加括号，就是把这个函数当作值来用
f = add                        # f 和 add 指向同一个函数
print(f(1, 2))                 # 3

# 函数可以作为参数传给另一个函数
def apply(func, x, y):
    return func(x, y)

print(apply(add, 3, 4))        # 7

# 函数也可以作为返回值（昨天闭包 + 今天装饰器的共同地基）


# ============================================================
# 三、手写第一个装饰器（重点）
# ============================================================
# 装饰器 = 接收函数 func，返回一个"增强版函数" wrapper
# 三步：接收 func → 定义 wrapper → 返回 wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)   # 真正执行原函数
        print("调用后")
        return result                    # 把结果原样交出去
    return wrapper                       # 注意：返回的是函数名，不加括号

@my_decorator
def say_hello(name):
    return f"你好，{name}"

print(say_hello("示其"))
# 输出：
# 调用前
# 调用后
# 你好，示其

# 【补充】wrapper 是什么？
#   wrapper = "包装纸/外套"的意思，是给原函数套上的那层新函数。
#   类比：原函数是一杯奶茶，wrapper 是装奶茶的杯套，杯套不影响奶茶本身，
#   但可以在杯套上印 logo（加功能）。


# ============================================================
# 四、@ 语法糖（重点）
# ============================================================
# @装饰器名 写在函数定义上面，相当于：
#   函数名 = 装饰器(函数名)
#
# 下面这两种写法完全等价：

# 写法 A：用 @
@my_decorator
def a1():
    return 1

# 写法 B：不用 @，手动替换
def a2():
    return 1
a2 = my_decorator(a2)

# 结论：@ 只是让代码更清爽，底层还是"把函数交给装饰器，再用返回的函数替换它"


# ============================================================
# 五、*args 与 **kwargs：接住任意参数（重点）
# ============================================================
# wrapper 里写 *args, **kwargs，是为了不管原函数要几个参数都能接住：
#   *args    把多余的位置参数打包成元组
#   **kwargs 把关键字参数打包成字典

def show_args(func):
    def wrapper(*args, **kwargs):
        print(f"收到的参数：{args} {kwargs}")
        return func(*args, **kwargs)     # 原样再传回给原函数
    return wrapper

@show_args
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

print(greet("示其", greeting="早上好"))
# 输出：
# 收到的参数：('示其',) {'greeting': '早上好'}
# 早上好，示其


# ============================================================
# 六、返回值的传递（重点，新手最容易忘）
# ============================================================
# wrapper 里必须 return func(*args, **kwargs)
# 如果忘了 return，装饰过的函数返回值会变成 None

def no_return_bug(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)            # 执行了，但没把结果交出去
    return wrapper

@no_return_bug
def add_bug(a, b):
    return a + b

print(add_bug(3, 4))            # None  ← 返回值丢了！

# 正确写法：wrapper 里 return func(...)
def fixed(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@fixed
def add_fixed(a, b):
    return a + b

print(add_fixed(3, 4))          # 7


# ============================================================
# 七、functools.wraps：保留原函数的"身份证"（重点）
# ============================================================
# 装饰后，原函数的 __name__（名字）、__doc__（文档说明）会丢，
# 因为对外暴露的是 wrapper，不是原函数。

import functools

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def add_1(a, b):
    "把两个数加起来"
    return a + b

print(add_1.__name__)           # wrapper   ← 名字丢了
print(add_1.__doc__)            # None      ← 文档说明也丢了

# 修复：在 wrapper 上面加一行 @functools.wraps(func)
def good_decorator(func):
    @functools.wraps(func)      # 把原函数的"身份证"复制到 wrapper 上
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def add_2(a, b):
    "把两个数加起来"
    return a + b

print(add_2.__name__)           # add_2   ← 恢复了
print(add_2.__doc__)            # 把两个数加起来

# 养成习惯：写装饰器时，wrapper 上面都加 @functools.wraps(func)


# ============================================================
# 八、计时装饰器（实用）
# ============================================================
import time

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"运行耗时：{end - start:.6f} 秒")
        return result
    return wrapper

@time_it
def slow_add(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(slow_add(1000000))
# 输出：
# 运行耗时：0.xxxxxx 秒
# 499999500000


# ============================================================
# 九、日志装饰器（实用）
# ============================================================
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"开始调用 {func.__name__}，参数：{args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"调用结束，返回：{result}")
        return result
    return wrapper

@log_call
def add_3(a, b):
    return a + b

print(add_3(2, 3))
# 输出：
# 开始调用 add_3，参数：(2, 3) {}
# 调用结束，返回：5
# 5


# ============================================================
# 十、装饰器里统计调用次数（进阶一点的小模式）
# ============================================================
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1        # 每次调用 +1
        return func(*args, **kwargs)
    wrapper.call_count = 0             # 给 wrapper 挂一个计数器
    return wrapper

@count_calls
def hi():
    return "hi"

hi()
hi()
hi()
print(hi.call_count)            # 3

# 关键点：函数也是一个对象，可以像给对象加属性一样给 wrapper 加 call_count


# ============================================================
# 十一、常见陷阱
# ============================================================
# 陷阱 1：装饰器最后忘了 return wrapper
#   def d(func):
#       def wrapper(...):
#           ...
#       # 这里忘写 return wrapper → 装饰后函数变成 None
#
# 陷阱 2：wrapper 里忘了 return func(...)
#   原函数的返回值会丢失，变成 None
#
# 陷阱 3：装饰器弄丢 __name__ / __doc__
#   用 @functools.wraps(func) 修复
#
# 陷阱 4：@ 语法糖只会执行一次（定义时替换），不是每次调用都套一层
#
# 陷阱 5：装饰器名字拼错 / 装饰器没定义就先使用


# ============================================================
# 十二、例题精讲（看懂了再去做练习）
# ============================================================

# ------------------------------------------------------------
# 例题 1：结果翻倍装饰器
# 题目：写 double_result，让被装饰函数的返回值乘以 2。
# 思路：wrapper 里先调用原函数拿到 result，再 return result * 2。
# ------------------------------------------------------------
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add_example(a, b):
    return a + b

print(add_example(1, 2))        # 6
print(add_example(10, 5))       # 30

# 关键点：先拿结果，再加工结果，最后 return 加工后的结果


# ------------------------------------------------------------
# 例题 2：结果转大写装饰器
# 题目：写 uppercase_result，让字符串返回值变成大写。
# 思路：拿到 result 后 str(result).upper() 再返回。
# ------------------------------------------------------------
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

@uppercase_result
def greet_example(name):
    return f"hello {name}"

print(greet_example("tom"))     # HELLO TOM

# 关键点：str() 先把结果转成字符串，再 upper()；对数字也能兜底不报错


# ------------------------------------------------------------
# 例题 3：计时装饰器（返回结果 + 耗时）
# 题目：写 time_it，让函数返回 (结果, 耗时) 元组。
# 思路：perf_counter 记开始和结束，相减得到耗时。
# ------------------------------------------------------------
import time

def time_it_example(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper

@time_it_example
def add_example2(a, b):
    return a + b

res, cost = add_example2(3, 4)
print(res)                      # 7
print(cost >= 0)                # True（耗时不可能为负数）

# 关键点：return 一个元组，调用时用 res, cost = ... 解包接住


# ------------------------------------------------------------
# 例题 4：调用次数统计装饰器
# 题目：写 count_calls，让被装饰函数可以 .call_count 查看调用次数。
# 思路：给 wrapper 挂一个 call_count 属性，每次调用自增。
# ------------------------------------------------------------
def count_calls_example(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls_example
def add_example3(a, b):
    return a + b

add_example3(1, 2)
add_example3(3, 4)
add_example3(5, 6)
print(add_example3.call_count)  # 3

# 关键点：wrapper 也是对象，可以自由挂属性当计数器用
