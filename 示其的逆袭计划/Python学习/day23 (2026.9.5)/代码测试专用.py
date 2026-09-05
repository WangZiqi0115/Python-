# Day 23 · 代码测试专用 (2026.9.5)
# 在这里随便写、随便试,不影响正式练习。
# 前提: 已 pip install numpy
# 运行: python "代码测试专用.py"

import numpy as np

#示例 1:创建一个数组,看看它长什么样
# a = np.array([1, 2, 3, 4])
# print("一维数组:", a)
# print("形状:", a.shape, "| 维度:", a.ndim, "| 类型:", a.dtype)

# # 示例 2:二维数组(矩阵)
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print("\n二维数组:\n", b)
# print("形状:", b.shape)          # (2, 3)

# # 示例 3:"调色"的本质 —— 对整组数字做运算
# img = np.array([[10, 20, 30],
#                 [40, 50, 60],
#                 [70, 80, 90]])
# print("\n原图(3x3像素亮度):\n", img)
# bright = img + 10                # 所有像素 +10 = "提亮"
# print("提亮 +10 后:\n", bright)

# # 示例 4:模拟 MNIST 一张 28x28 的图,拉平到 784
# img28 = np.random.rand(28, 28)
# flat = img28.reshape(28 * 28)
# print("\n28x28 图:", img28.shape, "→ 拉平后:", flat.shape)
# img = np.random.rand(28, 28)         # 模拟一张28x28的图
# flat = img.reshape(28 * 28)          # 拉平成784
# print("原图形状:", img.shape, "→ 拉平后:", flat.shape)
arr = np.arange(12)
new_arr = arr.reshape(3,4)
print(new_arr)
grid = np.arange(49).reshape(7, 7)
print(grid.reshape(49))
x = np.zeros((4,4))
y = np.ones((4,4))
print(x,"\n",y)
a = np.random.rand(28,28)
print(a,a.ndim,a.reshape(784))
scores = {"张三": 90, "李四": 85, "王五": 92, "赵六": 78}
scores = {"张三": 90, "李四": 85, "王五": 92, "赵六": 78}
print(sum(score for score in scores.values())/len(scores))