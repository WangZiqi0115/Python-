# # Day 25 · 代码测试专用 (2026.9.7)
# # 在这里随便写、随便试,不影响正式练习。
# # 前提: 已 pip install numpy
# # 运行: python "代码测试专用.py"

# import numpy as np

# # 示例 1:矩阵乘法 @ 基本形状
# # A = np.array([[1,2,3],[4,5,6]])      # (2,3)
# # B = np.array([[7,8],[9,10],[11,12]])  # (3,2)
# # print("A @ B:\n", A @ B)              # [[ 58  64]
# #                                        #  [139 154]]
# # print("形状:", (A @ B).shape)         # (2,2)

# # # 示例 2:@ 和 * 的区别
# # M = np.array([[1,2],[3,4]])
# # print("M @ M:\n", M @ M)     # 矩阵乘 [[ 7 10],[15 22]]
# # print("M * M:\n", M * M)     # 逐元素 [[ 1  4],[ 9 16]]

# # # 示例 3:转置 .T
# # P = np.array([[1,2,3],[4,5,6]])   # (2,3)
# # print("P.T:\n", P.T)              # (3,2)
# # print("形状:", P.T.shape)

# # # 示例 4:转置让维度对齐
# # X = np.random.rand(100, 784)
# # W = np.random.rand(784, 64)
# # print("X @ W 形状:", (X @ W).shape)    # (100, 64)

# # # 示例 5:前向传播 784 → 64 → 10
# # np.random.seed(1)
# # W1 = np.random.randn(64, 784)
# # b1 = np.random.randn(64)
# # W2 = np.random.randn(10, 64)
# # b2 = np.random.randn(10)
# # x = np.random.rand(784)
# # h = W1 @ x + b1
# # print("h 形状:", h.shape)              # (64,)
# # h1 = np.maximum(0, h)                  # ReLU激活(负数抹0)
# # z2 = W2 @ h1 + b2
# # print("输出形状:", z2.shape)           # (10,)
# # print("猜的数字:", int(np.argmax(z2)))
