# Day 17 · 代码测试专用 (2026.8.12)
# 在这里随便写、随便试，不影响正式练习。

# 示例：手动迭代
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))

# 示例：next 给默认值
print(next(it, "END"))

# 示例：自定义迭代器
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
    print(n)
