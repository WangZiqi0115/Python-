# Day 24 · 代码测试专用 (2026.9.6)
# 在这里随便写、随便试,不影响正式练习。
# 前提: 已 pip install numpy
# 运行: python "代码测试专用.py"

import numpy as np

# 示例 1:步长切片 —— 每隔一个取,以及倒着取
# a = np.arange(10)
# print("原数组:", a)
# print("隔一个取:", a[::2])        # [0 2 4 6 8]
# print("倒着取:", a[::-1])         # [9 8 7 6 5 4 3 2 1 0]

# # 示例 2:把 28x28 的"图"降采样成 14x14
# img = np.random.rand(28, 28)
# print("原图:", img.shape, "→ 降采样:", img[::2, ::2].shape)

# # 示例 3:布尔掩码 —— 二值化一张灰度图
# pixels = np.array([0, 129, 200, 40, 255, 90])
# print("掩码:", pixels > 100)
# print("大于100的:", pixels[pixels > 100])
# print("二值化:", np.where(pixels > 100, 255, 0))

# # 示例 4:花式索引 —— 按名单取样本(模拟洗牌)
# samples = np.array([100, 200, 300, 400, 500])
# order = np.array([4, 1, 0, 3, 2])
# print("洗牌后:", samples[order])

# # 示例 5:视图联动 vs copy 隔离
# m = np.arange(12).reshape(3, 4)
# sub = m[0:2, 0:2]          # 视图,会联动
# sub[0, 0] = 999
# print("改视图后原 m:\n", m)      # 会变
# m2 = np.arange(12).reshape(3, 4)
# safe = m2[0:2, 0:2].copy()
# safe[0, 0] = 999
# print("用copy后原 m2:\n", m2)     # 不变

# # 示例 6:多条件 与(&) 或(|)
# a = np.array([1, 5, 3, 8, 2])
# print("4到8之间:", a[(a > 4) & (a < 8)])   # [5]
# print("小于2或大于7:", a[(a < 2) | (a > 7)])   # [1 8]
