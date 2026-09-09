# # Day 26 · 代码测试专用 (2026.9.9)
# # 在这里随便写、随便试,不影响正式练习。
# # 前提: 已 pip install numpy
# # 运行: python "代码测试专用.py"

import numpy as np

# # 示例 1:广播 —— 每行加同一个向量(加偏置的真面目)
# a = np.array([[1.,2.],[3.,4.],[5.,6.]])     # (3,2)
# v = np.array([10., 20.])                    # (2,)
# print(a + v)        # 每行都加 [10,20]
# print(a + 100)      # 标量广播

# # 示例 2:广播报错 —— (3,2) 加 (3,) 对不上
# # try:
# #     np.array([[1.,2.],[3.,4.],[5.,6.]]) + np.array([10.,20.,30.])
# # except ValueError as e:
# #     print("报错:", e)

# # 示例 3:聚合 + axis
# g = np.array([[90.,85.,92.],[78.,88.,70.],[95.,60.,80.]])
# print(np.sum(g, axis=0))    # 每科总分 → [263. 233. 242.]
# print(np.mean(g, axis=1))   # 每人平均 → [89. 78.66666667 78.33333333]

# # 示例 4:argmax 猜数字
# probs = np.array([[0.1,0.05,0.7,0.15],[0.4,0.3,0.2,0.1]])
# print(np.argmax(probs, axis=1))   # [2 0]

# # 示例 5:seed 复现
# np.random.seed(42)
# print(np.random.rand(3))
# np.random.seed(42)
# print(np.random.rand(3))    # 一模一样

# # 示例 6:randint 造"像素图"
# img = np.random.randint(0, 256, size=(28, 28))
# print(img.shape, img.min(), img.max())

# # 示例 7:归一化 /255.0
# px = np.array([[0,128,255],[51,102,153]], dtype=np.uint8)
# n = px / 255.0
# print(n, n.min(), n.max())

# # 示例 8:keepdims 每行减自己的均值
# X = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
# m = X.mean(axis=1, keepdims=True)   # (3,1)
# print(X - m)
# print((X - m).mean(axis=1))         # ≈0
pr = np.array([[0.1, 0.7, 0.1, 0.1],    # 图0: 4类的概率
               [0.6, 0.2, 0.1, 0.1],    # 图1
               [0.2, 0.1, 0.6, 0.1],    # 图2
               [0.1, 0.2, 0.3, 0.4],    # 图3
               [0.25, 0.25, 0.25, 0.25]])  # 图4: 四个一样大
# 请在下方写代码:
#   (1) 算出每张图"概率最大的下标"(预测的数字),存进 pred 再 print
# 期望: [1 0 2 3 0]
#   (2) 在下方用一行注释回答: 为什么这里 axis 写 1,而不是 0?
# 提示: 每"行"是一张图,我们要把每行压成一个下标 → axis 写 1。
#       图4 四个概率一样大时,argmax 返回最靠前的那个下标 0。

print(np.argmax(pr,axis=1))
