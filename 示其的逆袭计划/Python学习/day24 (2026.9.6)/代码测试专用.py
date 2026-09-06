# # Day 24 · 代码测试专用 (2026.9.6)
# # 在这里随便写、随便试,不影响正式练习。
# # 前提: 已 pip install numpy
# # 运行: python "代码测试专用.py"

# import numpy as np

# # 示例 1:步长切片 —— 每隔一个取,以及倒着取
# # a = np.arange(10)
# # print("原数组:", a)
# # print("隔一个取:", a[::2])        # [0 2 4 6 8]
# # print("倒着取:", a[::-1])         # [9 8 7 6 5 4 3 2 1 0]

# # # 示例 2:把 28x28 的"图"降采样成 14x14
# # img = np.random.rand(28, 28)
# # print("原图:", img.shape, "→ 降采样:", img[::2, ::2].shape)

# # # 示例 3:布尔掩码 —— 二值化一张灰度图
# # pixels = np.array([0, 129, 200, 40, 255, 90])
# # print("掩码:", pixels > 100)
# # print("大于100的:", pixels[pixels > 100])
# # print("二值化:", np.where(pixels > 100, 255, 0))

# # # 示例 4:花式索引 —— 按名单取样本(模拟洗牌)
# # samples = np.array([100, 200, 300, 400, 500])
# # order = np.array([4, 1, 0, 3, 2])
# # print("洗牌后:", samples[order])

# # # 示例 5:视图联动 vs copy 隔离
# # m = np.arange(12).reshape(3, 4)
# # sub = m[0:2, 0:2]          # 视图,会联动
# # sub[0, 0] = 999
# # print("改视图后原 m:\n", m)      # 会变
# # m2 = np.arange(12).reshape(3, 4)
# # safe = m2[0:2, 0:2].copy()
# # safe[0, 0] = 999
# # print("用copy后原 m2:\n", m2)     # 不变

# # # 示例 6:多条件 与(&) 或(|)
# # a = np.array([1, 5, 3, 8, 2])
# # print("4到8之间:", a[(a > 4) & (a < 8)])   # [5]
# # print("小于2或大于7:", a[(a < 2) | (a > 7)])   # [1 8]
# img = np.array([[0, 129, 200, 40],
#                 [255, 30, 90, 160],
#                 [80, 210, 15, 250],
#                 [7, 128, 64, 190]])
# print("\n一张 4x4 的灰度图:\n", img)
# white = img >= 128                 # 掩码: 亮度≥128 记True(视为"白")
# print("≥128 的掩码:\n", white.astype(int))
# arr = np.array([10, 20, 30, 40, 50])
# print("arr =", arr)
# print("arr[[3,1]] =", arr[[3, 1]])          # [40 20]
# m2 = np.arange(12).reshape(3, 4)
# print("\nm2:\n", m2)
# print("取第2行、第0行:\n", m2[[2, 0]])
# m3 = np.arange(9).reshape(3, 3)
# print("原 m3:\n", m3)
# sub = m3[0:2, 0:2]      # 基本切片 → 视图
# sub[0, 0] = 99
# print("改过 sub 后,原 m3:\n", m3)   
# m4 = np.arange(9).reshape(3, 3)
# sub2 = m4[0:2, 0:2].copy()
# sub2[0, 0] = 99
# print("\n用 .copy() 后,原 m4:\n", m4) 
# print(sub2)
# img2 = np.array([[60, 180], [250, 30]])
# #   ↑ 示其提问(2026.9.6):这么横着写的数组是一维还是二维?
# #   答:二维(2行2列)。判断维度看"中括号包了几层",不是看是不是横着写。
# #     np.array([60,180])          → 1层括号 → 一维,2个元素
# #     np.array([[60,180],[250,30]])→ 2层括号 → 二维,2行2列 → shape(2,2)
# #   横着写/竖着写只是排版,Python不区分;写成两行也一样是二维。
# #   记法: 数中括号层数 = ndim(几维)。实测 img2.shape=(2,2),img2.ndim=2。
# img2 >= 128                    # [[False  True  True False]]
# binary = np.where(img2 >= 128, 255, 0)
# print("\n例题2 原灰度图:\n", img2)
# print("二值化后:\n", binary)
# # [[  0 255]
# #  [255   0]]
# arr25 = np.arange(25).reshape(5, 5)
# # 请在下方写代码(用 [::2, ::2] 这种步长写法,print 出来)
# # 期望输出是这个 3x3 的棋盘格:
# # [[ 0  2  4]
# #  [10 12 14]
# #  [20 22 24]]
# print(arr25[::2,::2])
# pixels = np.array([0, 129, 200, 40, 255, 90])
# # 请在下方写代码:
# #   (1) 先 print(pixels > 100) 看掩码长什么样
# #   (2) 再 print(pixels[pixels > 100]) 找出那些数
# # 期望: 掩码 [False  True  True False  True False];找出的数是 [129 200 255]
# print(pixels > 100)
# print(pixels[pixels > 100])

# ============================================================
# 练习 4 · np.where 二值化(10 分)
# 用 np.where 把练习3那行像素"二值化":大于100的变255,否则变0
# ============================================================
# 提示: np.where(①条件, ②满足给的值, ③不满足给的值)
# 请在下方写代码(print 结果)
# 期望输出: [  0 255 255   0 255   0]


s = "AI 你好"
b = s.encode("utf-8")
print(b.decode("gbk"))    # 输出一堆乱码，不报错 → 选C