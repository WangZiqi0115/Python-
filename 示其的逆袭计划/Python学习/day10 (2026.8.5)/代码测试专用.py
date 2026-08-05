"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 10 准备就绪！")
# import sys

# big_list = [x for x in range(1000000)]       # 列表：立刻算出100万个
# big_gen = (x for x in range(1000000))        # 生成器：先不算，用的时候再给

# print(sys.getsizeof(big_list) )   # 大约 8MB（100万个数字都存着）
# print(sys.getsizeof(big_gen))     # 大约 112B（几乎不占内存）
l =[" 95 ", "", " 87", "92 ", "  "]
lines =[int(num.strip()) for num in l if num.strip()]
print(lines)
