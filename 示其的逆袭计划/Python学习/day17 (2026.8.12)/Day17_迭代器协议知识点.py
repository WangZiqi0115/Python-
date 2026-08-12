# Day 17 · 迭代器协议 知识点速查 (2026.8.12)
# ============================================
# 今天搞懂 for 循环的底层：iter / next / StopIteration。
# 这也是理解生成器、大文件读取、自定义数据结构的基础。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。


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
# 一个类想支持 for 循环，要实现两个方法：
#   __iter__()   返回迭代器（通常返回 self）
#   __next__()   返回下一个元素；没得取了就抛 StopIteration

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n)              # 3 2 1

# 也可以用生成器函数实现同样的效果（Day 10 学过 yield）：
def gen_countdown(start):
    while start > 0:
        yield start
        start -= 1

print(list(gen_countdown(3)))          # [3, 2, 1]


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
