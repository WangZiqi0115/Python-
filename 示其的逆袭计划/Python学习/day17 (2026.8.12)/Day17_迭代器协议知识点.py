# Day 17 · 迭代器协议 知识点速查 (2026.8.12)
# ============================================
# 今天搞懂 for 循环的底层：iter / next / StopIteration。
# 这也是理解生成器、大文件读取、自定义数据结构的基础。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。

# 【补充】文件名里的"协议"是什么意思？
#   协议 = 一套约定好的规则
#   Python 迭代器协议规定：
#     1. 对象提供 __iter__()，返回一个迭代器
#     2. 对象提供 __next__()，每次返回下一个元素，没得取就抛 StopIteration
#   只要遵守这套约定，for / next / list / sum 等工具就都能统一使用它
#   类比：插座协议 = 标准三孔，不管什么电器，插头符合就能用

# 【补充】迭代器大白话总览（发糖果比喻）：
#   [10, 20, 30] 像一盒糖，里面装着三颗，随时能看、能数
#   iter(nums)  = 把盒子交给"发糖机器"，机器记住现在该发第几颗
#   next(机器)  = 机器递给你下一颗糖，然后自动指向下一颗
#   StopIteration = 机器说"没了，发完了"，队伍结束
#   for x in nums = 机器自动一颗颗发到你手里，发完自动停
#   生成器 = 机器不提前准备整盒糖，而是现场变出下一颗，所以省内存
#   一句话：
#     可迭代对象 = 装数据的东西
#     迭代器 = 记住进度、一次给一个的机器
#     iter = 造机器；next = 让机器给一个；StopIteration = 给完了
#     for = 让机器自动发到结束


# ============================================================
# 一、可迭代对象（iterable）
# ============================================================
# 能用 for 循环"一个一个取出元素"的对象，就是可迭代对象
#   list、tuple、dict、set、str、range、文件对象...

for x in [1, 2, 3]:
    print(x)

for ch in "abc":
    print(ch)

for i in range(3):
    print(i)

# 字典默认迭代的是"键"：
d = {"name": "张三", "age": 18}
for key in d:
    print(key)          # name / age


# ============================================================
# 二、迭代器（iterator）是什么
# ============================================================
# 迭代器 = 一个"知道现在走到哪了"的对象
#   它一次只能取一个，取完一个自动指向下一个

# 用 iter() 把可迭代对象变成迭代器：
nums = [10, 20, 30]
it = iter(nums)
print(type(it))          # <class 'list_iterator'>

# 用 next() 手动取下一个：
print(next(it))          # 10
print(next(it))          # 20
print(next(it))          # 30

# 取完后再 next 会抛 StopIteration：
# print(next(it))        # ❌ StopIteration


# ============================================================
# 三、for 循环的底层原理（重点）
# ============================================================
# for x in 可迭代对象 其实做了三件事：
#   1. iter() 拿到迭代器
#   2. 不断 next() 取元素
#   3. 遇到 StopIteration 就结束循环

# 下面的代码等价于 for x in nums:
it2 = iter([1, 2, 3])
while True:
    try:
        x = next(it2)
        print(x)
    except StopIteration:
        break

# 记牢这个流程，后面看生成器、自定义迭代器就很容易


# ============================================================
# 四、next() 的默认值
# ============================================================
# next(迭代器, 默认值)：没有下一个时返回默认值，不抛异常
it3 = iter([1, 2])
print(next(it3, "END"))   # 1
print(next(it3, "END"))   # 2
print(next(it3, "END"))   # END


# ============================================================
# 五、迭代器是一次性的（重点）
# ============================================================
it4 = iter([1, 2, 3])
print(list(it4))          # [1, 2, 3]
print(list(it4))          # []  第二次是空的！

# 原因：迭代器像"单向前进的传送带"，走过就没了
# 需要重复遍历就重新 iter()，或用列表存起来


# ============================================================
# 六、常见迭代器 / 可迭代对象
# ============================================================
# map / filter / zip / enumerate / reversed 返回的都是迭代器

print(list(map(str, [1, 2, 3])))       # ['1', '2', '3']
print(list(filter(lambda x: x > 1, [1, 2, 3])))  # [2, 3]
print(list(zip([1, 2], ["a", "b"])))   # [(1, 'a'), (2, 'b')]
print(list(enumerate(["a", "b"])))     # [(0, 'a'), (1, 'b')]
print(list(reversed([1, 2, 3])))       # [3, 2, 1]

# 文件对象也是可迭代的：for line in f 逐行读，不占内存


# ============================================================
# 七、自定义迭代器（重点）
# ============================================================
# 【补充】下面的 class 还没有系统学过，先这样理解：
#   class = "模板"，Countdown(3) 按模板造出一个倒计时对象
#   __init__ = 造对象时自动执行的初始化，self.current = start 存起始值
#   __iter__ = 告诉 Python"我能被 for 循环"，返回 self
#   __next__ = 每次取下一个元素时执行，取完抛 StopIteration
#   今天会照抄、能看懂结构就行；OOP 系统学习在 Day 32
# 一个类想支持 for 循环，要实现两个方法：
#   __iter__()   返回迭代器（通常返回 self）
#   __next__()   返回下一个元素；没得取了就抛 StopIteration

class Countdown:                    # 定义模板：这个类叫 Countdown（倒计时）
    def __init__(self, start):      # 创建对象时自动执行的方法，start 是传入的起始值
        self.current = start        # 把起始值记在这个对象身上，变量名叫 current

    def __iter__(self):             # 让这个对象能被 for 循环的方法
        return self                 # 返回自己，意思是"我自己就是迭代器"

    def __next__(self):             # 每次 for 循环要下一个元素时执行
        if self.current <= 0:       # 如果当前值已经 <= 0，说明没得数了
            raise StopIteration     # 抛出"没有更多元素"的信号，for 循环收到后结束
        value = self.current        # 先把当前值存到 value 里
        self.current -= 1           # 当前值减 1，为下一次做准备
        return value                # 把 value 交给 for 循环

for n in Countdown(3):              # 造一个起始值为 3 的倒计时对象，for 自动调用 __iter__/__next__
    print(n)                        # 依次打印 3、2、1

# 也可以用生成器函数实现同样的效果（Day 10 学过 yield）：
def gen_countdown(start):
    while start > 0:
        yield start
        start -= 1

print(list(gen_countdown(3)))          # [3, 2, 1]

# 【补充】yield 是什么？
#   yield = "暂停并交出一个值，下次调用继续"
#   对比 return：return 直接结束函数；yield 只是暂停，还会回来
#   含 yield 的函数被调用时不执行函数体，而是返回一个生成器对象
#   gen_countdown(3) 的执行过程：
#     第 1 次 next → start=3>0 → yield 3 → 暂停
#     第 2 次 next → 继续：start-=1 → 2 → yield 2 → 暂停
#     第 3 次 next → 继续：start-=1 → 1 → yield 1 → 暂停
#     第 4 次 next → 继续：start-=1 → 0 → while 结束 → StopIteration
#   list(gen_countdown(3)) 自动迭代，得到 [3, 2, 1]
#   生成器 = Python 自动实现 __iter__/__next__ 的迭代器，省去手写类


# ============================================================
# 八、可迭代对象 vs 迭代器
# ============================================================
# 可迭代对象（iterable）：能 iter() 的，比如 list
# 迭代器（iterator）：既能 iter() 又能 next() 的

# iter(迭代器) 返回它自己：
it5 = iter([1, 2, 3])
print(it5 is iter(it5))   # True

# 判断一个对象是不是迭代器：看有没有 __next__
print(hasattr(it5, "__next__"))        # True
print(hasattr([1, 2, 3], "__next__"))  # False，列表不是迭代器


# ============================================================
# 九、实战场景
# ============================================================
# 1. 手动只取前几个元素：
#    it = iter(big_list); first = next(it); second = next(it)

# 2. 大文件逐行处理：
#    with open("data.txt", encoding="utf-8") as f:
#        for line in f:
#            ...

# 3. 自定义数据结构支持 for：
#    实现 __iter__ / __next__ 后，就能 for 遍历

# 4. 结合生成器做"懒加载"：
#    数据量大时不一次性算完，用迭代器慢慢给


# ============================================================
# 十、常见陷阱
# ============================================================
# 陷阱 1：迭代器只能用一次
#   it = iter([1,2,3]); list(it); list(it) → []（第二次空）
#   需要多次使用就重新 iter()

# 陷阱 2：next 取完会抛 StopIteration
#   不确定有没有下一个时，用 next(it, 默认值)

# 陷阱 3：字典 for 默认只迭代键
#   想遍历键值对：for k, v in d.items()

# 陷阱 4：map/filter/zip 返回的是迭代器
#   不套 list() 直接打印，看到的是 <map object ...>

# 陷阱 5：迭代过程中修改列表可能出问题
#   遍历时不要随便 append/remove，先收集到新列表


# ============================================================
# 十一、例题精讲（看懂了再去做练习）
# ============================================================

# ------------------------------------------------------------
# 例题 1：用 iter / next 取第一个和最后一个
# 题目：nums = [5, 10, 15, 20]，不直接用 nums[0] / nums[-1]，
#       用迭代器取出 (第一个, 最后一个)
# 思路：先 next 拿第一个；然后一直 next，每拿到一个就更新 last，
#       直到抛 StopIteration，此时 last 就是最后一个
# ------------------------------------------------------------
def first_and_last(nums):
    it = iter(nums)              # 造发糖机器
    first = next(it)             # 第一颗糖
    last = first                 # 先假设只有一个元素
    while True:
        try:
            last = next(it)      # 继续拿下一颗，更新 last
        except StopIteration:
            break                # 没糖了，结束
    return first, last

print(first_and_last([5, 10, 15, 20]))   # (5, 20)

# 关键点：StopIteration 不是错误，而是"发完了"的结束信号


# ------------------------------------------------------------
# 例题 2：自定义迭代器输出偶数
# 题目：写一个 Evens 类，从 0 开始依次给出偶数，最多给 count 个
# 思路：__iter__ 返回 self；__next__ 里先判断给没给够，
#       给够了就抛 StopIteration，否则返回当前偶数并 +2
# ------------------------------------------------------------
class Evens:
    def __init__(self, count):
        self.count = count       # 最多给几个
        self.given = 0           # 已经给了几个
        self.value = 0           # 下一个要给的偶数

    def __iter__(self):
        return self

    def __next__(self):
        if self.given >= self.count:
            raise StopIteration
        result = self.value
        self.value += 2
        self.given += 1
        return result

print(list(Evens(4)))            # [0, 2, 4, 6]

# 关键点：每次 __next__ 都要更新"进度"，否则会无限循环


# ------------------------------------------------------------
# 例题 3：生成器版斐波那契
# 题目：用 yield 写 fib(n)，产生前 n 个斐波那契数
# 思路：a, b 从 0, 1 开始；每次 yield 当前的 a，
#       然后 a, b = b, a + b 递推下一个
# ------------------------------------------------------------
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(6)))              # [0, 1, 1, 2, 3, 5]

# 关键点：yield 让函数变成生成器，for / list 会不断 next 它


# ------------------------------------------------------------
# 例题 4：next 默认值实现"按块取数"
# 题目：it = iter([1, 2, 3, 4, 5])，每次取 2 个，不足 2 个就返回 None
# 思路：用 next(it, None) 安全取数，取不到返回 None
# ------------------------------------------------------------
it_demo = iter([1, 2, 3, 4, 5])

block1 = (next(it_demo, None), next(it_demo, None))   # (1, 2)
block2 = (next(it_demo, None), next(it_demo, None))   # (3, 4)
block3 = (next(it_demo, None), next(it_demo, None))   # (5, None)

print(block1)                    # (1, 2)
print(block2)                    # (3, 4)
print(block3)                    # (5, None)

# 关键点：next(it, 默认值) 在取不到时不会抛异常，很适合处理"可能不够"的数据
