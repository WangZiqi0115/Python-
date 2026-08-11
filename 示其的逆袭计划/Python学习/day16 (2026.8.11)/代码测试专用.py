# Day 16 · 代码测试专用 (2026.8.11)
# 在这里随便写、随便试，不影响正式练习。

# 示例：星号解包
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first, middle, last)

# 示例：调用解包
print(*nums)

# 示例：转置
pairs = [(1, 4), (2, 5), (3, 6)]
print(list(zip(*pairs)))
