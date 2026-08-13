# Day 18 · 代码测试专用 (2026.8.13)
# 在这里随便写、随便试，不影响正式练习。

# 示例：闭包
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_5 = make_adder(5)
print(add_5(3))

# 示例：nonlocal 计数器
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())
print(c())
