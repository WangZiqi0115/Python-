# # Day 27 · 代码测试专用 (2026.9.10)
# # 在这里随便写、随便试,不影响正式练习。
# # 前提: 已 pip install numpy
# # 运行: python "代码测试专用.py"

# import numpy as np

# # 示例 1:造数据集 + 查形状(X 行数必须 = y 长度)
# X = np.array([[10.,20.,30.,40.],[50.,60.,70.,80.],[90.,10.,20.,30.],
#               [40.,50.,60.,70.],[20.,30.,40.,50.],[80.,70.,60.,50.]])
# y = np.array([0,1,0,1,0,1])
# print(X.shape, y.shape, X.shape[0] == len(y))      # (6, 4) (6,) True

# # 示例 2:8:2 划分(洗牌 + 切片,X 和 y 用同一份下标)
# np.random.seed(0)
# n = X.shape[0]
# idx = np.random.permutation(n)
# cut = int(n * 0.8)
# print(idx, cut)                                    # [5 2 1 3 0 4] 4
# print(X[idx[:cut]].shape, y[idx[:cut]].shape)      # (4, 4) (4,)
# print(X[idx[cut:]].shape, y[idx[cut:]].shape)      # (2, 4) (2,)

# # 示例 3:算准确率
# y_true = np.array([3,1,4,1,5])
# pred = np.array([3,0,4,2,5])
# print((pred == y_true).sum(), (pred == y_true).mean())   # 3 0.6

# # 示例 4:看标签分布
# y2 = np.array([0,1,1,2,0,3,0,1])
# vals, counts = np.unique(y2, return_counts=True)
# print(vals, counts)                                # [0 1 2 3] [3 3 1 1]

# # 示例 5:分批
# fake = np.arange(20).reshape(20, 1)
# bs = 8
# print(fake[0:bs].ravel())                          # 第0批
# print(20 // bs, 20 % bs)                           # 2 批,余 4 个

# # 示例 6:装饰器回顾(Day 19)
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("调用", func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
# @log
# def add(a, b):
#     return a + b
# print(add(1, 2))
