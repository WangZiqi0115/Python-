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

# 【补充】my_decorator 到底做了什么？（装饰器的核心骨架）
#  1. 接收一个"函数"当参数：func = 被装饰的原函数（比如 say_hello）
#  2. 在内部造一个新函数 wrapper：在原函数执行前/后各打印一句，结果原样返回
#  3. 最后 return wrapper：把"套好外套"的新函数交出去，替换原函数
#  一句话：装饰器 = "接收函数、返回函数"的函数；不改原函数内部代码，只在外面加功能。
#  配合 @my_decorator 使用：@my_decorator 等价于 say_hello = my_decorator(say_hello)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 【补充】这里的 *args 和 **kwargs 是什么意思？
        #   *args    把"所有多余的位置参数"打包成元组 args，如 say_hello("示其")
        #   **kwargs 把"所有多余的关键字参数"打包成字典 kwargs，如 greet(name="示其")
        #   合在一起 = wrapper 不管原函数要几个参数，都能"照单全收"
        #   下面 func(*args, **kwargs) 是"拆包转交"：定义里 * 是打包，调用里 * 是拆开，
        #   参数原样传给原函数。详细讲解见下方"五、*args 与 **kwargs：接住任意参数"
        print("调用前")
        result = func(*args, **kwargs)   # 真正执行原函数
        print("调用后")
        return result                    # 把结果原样交出去
    return wrapper                       # 注意：返回的是函数名，不加括号

# 【补充】@ 是什么意思？（语法糖）
#   @my_decorator 等价于：say_hello = my_decorator(say_hello)
#   意思是：把 say_hello 这个函数交给 my_decorator 加工，
#   用返回的新函数（带"调用前/调用后"打印的那个）替换掉原来的名字。
#   注意：@ 必须写在函数定义正上方；替换发生在"定义时"（一次性），不是每次调用。
@my_decorator
def say_hello(name):
    return f"你好，{name}"

# 【补充】这里的 say_hello 被装饰后，里面装的是 wrapper：
#   执行 print(say_hello("示其")) 时实际依次做 4 件事：
#     ① print("调用前")
#     ② 调用原来的 say_hello("示其")，得到 "你好，示其" 存进 result
#     ③ print("调用后")
#     ④ 把 result 返回给外面的 print
#   所以最终输出才是下面那三行：调用前 / 调用后 / 你好，示其
print(say_hello("示其"))
# 输出：
# 调用前
# 调用后
# 你好，示其

# 【补充】wrapper 是什么？
#   wrapper = "包装纸/外套"的意思，是给原函数套上的那层新函数。
#   类比：原函数是一杯奶茶，wrapper 是装奶茶的杯套，杯套不影响奶茶本身，
#   但可以在杯套上印 logo（加功能）。
# 【补充】没有 wrapper 行不行？—— 不行！
#   Python 无法往已定义好的函数里"塞"新代码，想加功能只能新建一个函数把它包住
#   装饰器 = 接收函数 → 造 wrapper → 返回 wrapper；wrapper 就是"装饰后的成品"
#   反例 1：def d(func): return func（不造 wrapper）→ 加了等于没加
#   反例 2：def d(func): return "字符串"（返回的不是函数）→ 调用时报 TypeError


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

# 【补充】这两段代码的运行流程（A 和 B 完全等价）：
#   写法 A：① 定义函数 a1（body = return 1）
#           ② Python 看到 @my_decorator，调用 my_decorator(a1) 得到 wrapper
#           ③ 把 wrapper 重新绑定到名字 a1
#   写法 B：① 定义函数 a2（body = return 1）
#           ② 手动调用 my_decorator(a2) 得到 wrapper
#           ③ 赋值 a2 = wrapper
#   结论：@ 只是帮你少写一行 a1 = my_decorator(a1)，两种写法结果完全一样

# 结论：@ 只是让代码更清爽，底层还是"把函数交给装饰器，再用返回的函数替换它"


# ============================================================
# 五、*args 与 **kwargs：接住任意参数（重点）
# ============================================================
# wrapper 里写 *args, **kwargs，是为了不管原函数要几个参数都能接住：
#   *args    把多余的位置参数打包成元组
#   **kwargs 把关键字参数打包成字典

# 【补充】这个 func 是什么？
#   func 是 show_args 的形参（参数占位符），不是在这里"定义函数"
#   它专门接收"被装饰的原函数"：
#     @show_args 装饰 greet 时，Python 会执行 show_args(greet)，于是 func = greet
#   第 149 行 func(*args, **kwargs) 就是在调用 greet 本身（把参数原样传回去）
#   注意：wrapper 里用的 func 就是外面这个 func（靠闭包传进去，昨天学的）
def show_args(func):
    def wrapper(*args, **kwargs):
        print(f"收到的参数：{args} {kwargs}")
        return func(*args, **kwargs)     # 原样再传回给原函数
    return wrapper

@show_args
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

# 【补充】对！本质就是这样：@show_args 装饰 greet 时，Python 执行 greet = show_args(greet)
#   ① show_args(greet)：形参 func 指向"原来的 greet 函数"
#   ② show_args 返回 wrapper，再赋值回 greet → greet 这个名字指向 wrapper
#   所以最后：func 指向"原来的 greet"（被 wrapper 闭包记住）；greet 指向 wrapper
#   调用 greet("示其", ...) 时走 wrapper，wrapper 内部通过 func 调用原函数

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
import time                                     # 导入 time 模块，用来获取精确时间

def time_it(func):                              # 装饰器：接收原函数 func
    @functools.wraps(func)                      # 保留原函数的 __name__/__doc__（"身份证"）
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        start = time.perf_counter()             # 记录"开始"的精确时间
        result = func(*args, **kwargs)          # 真正调用原函数，把结果存进 result
        end = time.perf_counter()               # 记录"结束"的精确时间
        print(f"运行耗时：{end - start:.6f} 秒")   # 打印耗时 = 结束 - 开始，保留 6 位小数
        return result                           # 把原函数的结果原样返回
    return wrapper                              # 把包装函数交出去（替换原函数）

@time_it                                        # 语法糖：slow_add = time_it(slow_add)
def slow_add(n):                                # 定义一个"慢"的求和函数
    total = 0                                   # 累加器初始值为 0
    for i in range(n):                          # 循环 n 次，i 从 0 到 n-1
        total += i                              # 把当前的 i 累加进 total
    return total                                # 返回累加结果

print(slow_add(1000000))                        # 调用装饰后的函数：先打印耗时，再返回结果
# 输出：
# 运行耗时：0.xxxxxx 秒
# 499999500000


# ============================================================
# 九、日志装饰器（实用）
# ============================================================
def log_call(func):                             # 装饰器：接收原函数 func
    @functools.wraps(func)                      # 保留原函数的 __name__/__doc__
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        print(f"开始调用 {func.__name__}，参数：{args} {kwargs}")  # 打印：函数名 + 收到的参数
        result = func(*args, **kwargs)          # 真正调用原函数，把结果存进 result
        print(f"调用结束，返回：{result}")         # 打印：原函数返回的结果
        return result                           # 把结果原样返回
    return wrapper                              # 把包装函数交出去

@log_call                                       # 语法糖：add_3 = log_call(add_3)
def add_3(a, b):                                # 定义一个加法函数
    return a + b                                # 返回 a + b

print(add_3(2, 3))                              # 调用装饰后的函数：先打印日志，再返回 5
# 输出：
# 开始调用 add_3，参数：(2, 3) {}
# 调用结束，返回：5
# 5


# ============================================================
# 十、装饰器里统计调用次数（进阶一点的小模式）
# ============================================================
def count_calls(func):                          # 装饰器：接收原函数 func
    def wrapper(*args, **kwargs):               # 定义包装函数
        wrapper.call_count += 1                 # 每次被调用，计数器 +1
        return func(*args, **kwargs)            # 调用原函数并返回结果
    wrapper.call_count = 0                      # 给 wrapper 挂一个计数器，初始值为 0
    return wrapper                              # 把包装函数交出去

@count_calls                                    # 语法糖：hi = count_calls(hi)
def hi():                                       # 定义一个简单函数
    return "hi"                                 # 返回字符串 "hi"

hi()                                            # 第 1 次调用 → call_count 变成 1
hi()                                            # 第 2 次调用 → call_count 变成 2
hi()                                            # 第 3 次调用 → call_count 变成 3
print(hi.call_count)            # 3             # 打印调用次数 → 3

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
def double_result(func):                        # 装饰器：接收原函数 func
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        result = func(*args, **kwargs)          # 调用原函数，拿到结果
        return result * 2                       # 把结果 ×2 再返回
    return wrapper                              # 把包装函数交出去

@double_result                                  # 语法糖：add_example = double_result(add_example)
def add_example(a, b):                          # 定义加法函数
    return a + b                                # 返回 a + b

print(add_example(1, 2))        # 6             # 装饰后：(1+2)*2 = 6
print(add_example(10, 5))       # 30            # 装饰后：(10+5)*2 = 30

# 关键点：先拿结果，再加工结果，最后 return 加工后的结果


# ------------------------------------------------------------
# 例题 2：结果转大写装饰器
# 题目：写 uppercase_result，让字符串返回值变成大写。
# 思路：拿到 result 后 str(result).upper() 再返回。
# ------------------------------------------------------------
def uppercase_result(func):                     # 装饰器：接收原函数 func
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        result = func(*args, **kwargs)          # 调用原函数，拿到结果
        return str(result).upper()              # 转成字符串再变大写，返回
    return wrapper                              # 把包装函数交出去

@uppercase_result                               # 语法糖：greet_example = uppercase_result(greet_example)
def greet_example(name):                        # 定义问候函数
    return f"hello {name}"                      # 返回 "hello 名字"

print(greet_example("tom"))     # HELLO TOM    # 装饰后：结果转大写输出

# 关键点：str() 先把结果转成字符串，再 upper()；对数字也能兜底不报错


# ------------------------------------------------------------
# 例题 3：计时装饰器（返回结果 + 耗时）
# 题目：写 time_it，让函数返回 (结果, 耗时) 元组。
# 思路：perf_counter 记开始和结束，相减得到耗时。
# ------------------------------------------------------------
import time                                     # 导入 time 模块，用来取精确时间

def time_it_example(func):                      # 装饰器：接收原函数 func
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        start = time.perf_counter()             # 记录开始时间
        result = func(*args, **kwargs)          # 调用原函数，拿到结果
        end = time.perf_counter()               # 记录结束时间
        return result, end - start              # 返回元组 (结果, 耗时)
    return wrapper                              # 把包装函数交出去

@time_it_example                                # 语法糖：add_example2 = time_it_example(add_example2)
def add_example2(a, b):                         # 定义加法函数
    return a + b                                # 返回 a + b

res, cost = add_example2(3, 4)                  # 用解包接住返回的 (结果, 耗时)

# 【补充】为什么"逗号后面还能有内容"？—— 元组 + 解包
#   return result, end - start：return 后面跟两个值（用逗号隔开），
#     会自动打包成一个"元组" (result, 耗时) 返回
#   res, cost = add_example2(3, 4)：左边两个变量用逗号隔开，
#     会把返回的元组"拆开"，分别装进 res 和 cost（这叫解包 unpacking）
#   所以逗号不是多余，正是 Python 创建/拆开元组的语法
print(res)                      # 7             # 打印结果 → 7
print(cost >= 0)                # True          # 耗时不可能为负数 → True

# 关键点：return 一个元组，调用时用 res, cost = ... 解包接住


# ------------------------------------------------------------
# 例题 4：调用次数统计装饰器
# 题目：写 count_calls，让被装饰函数可以 .call_count 查看调用次数。
# 思路：给 wrapper 挂一个 call_count 属性，每次调用自增。
# ------------------------------------------------------------
def count_calls_example(func):                  # 装饰器：接收原函数 func
    def wrapper(*args, **kwargs):               # 定义包装函数：收下所有参数
        wrapper.call_count += 1                 # 每次调用计数 +1
        return func(*args, **kwargs)            # 调用原函数并返回结果
    wrapper.call_count = 0                      # 给 wrapper 挂计数器，初始值为 0
    return wrapper                              # 把包装函数交出去

@count_calls_example                            # 语法糖：add_example3 = count_calls_example(add_example3)
def add_example3(a, b):                         # 定义加法函数
    return a + b                                # 返回 a + b

add_example3(1, 2)                              # 第 1 次调用
add_example3(3, 4)                              # 第 2 次调用
add_example3(5, 6)                              # 第 3 次调用
print(add_example3.call_count)  # 3             # 打印调用次数 → 3

# 关键点：wrapper 也是对象，可以自由挂属性当计数器用
