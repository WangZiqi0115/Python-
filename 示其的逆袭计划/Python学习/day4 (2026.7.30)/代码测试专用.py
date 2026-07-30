"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

import time
# 导入 time 模块，用来计算代码运行时间
big_list = list(range(1000000))
# 创建一个包含 0~999999 的列表，共 100 万个元素
big_set = set(big_list)
# 把列表转成集合，得到同样的 100 万个元素

# 列表查找
start = time.time()
# 记录当前时间（开始计时）
999999 in big_list
# 在列表中查找 999999 是否存在
print("列表查找:", time.time() - start)
# 打印"列表查找: 花费的时间"

# 集合查找
start = time.time()
# 记录当前时间（开始计时）
999999 in big_set
# 在集合中查找 999999 是否存在
print("集合查找:", time.time() - start)
# 打印"集合查找: 花费的时间"