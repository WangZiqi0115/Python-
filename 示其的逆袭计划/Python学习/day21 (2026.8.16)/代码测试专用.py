# Day 21 · 代码测试专用 (2026.8.16)
# 在这里随便写、随便试，不影响正式练习。

# # 示例：试试 try/except/else/finally 四兄弟
# def demo(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "出错了"
#     else:
#         return f"成功：{result}"
#     finally:
#         print("收尾")
#
# print(demo(10, 2))
# print(demo(1, 0))

# # 示例：试试 raise
# def set_age(age):
#     if age < 0:
#         raise ValueError("年龄不能为负")
#     return age

# print("Day 21 代码测试专用")
# def check_positive(x):
#     assert x > 0, f"{x} 不是正数"     # 条件 False → AssertionError
#     return f"{x} 是正数"

# print(check_positive(5))13+6+4
# """6,2,3,4,5,5
# 624 355
# 624
# 6 24
# 24
# 2"""
# dct1 = {"a": 1,"b":1}
# dct2 = {"b": 1,"a":1}
# print
s = "   fly me   to   the moon  "

print(len(s.strip().split()[-1]))



    
        