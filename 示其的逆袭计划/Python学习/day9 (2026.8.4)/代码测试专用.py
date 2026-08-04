"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 9 准备就绪！")
# def Hello_World(text):
#     print(text)
# Hello_World("print")
# import math
# s = math.pi
# print(s)
import random
target = random.randint(1, 20)
attempts = 0
    # 请在此处编写代码
# while True:
#         num = int(input("请输入1-20之间的数字\n"))
#         if num > target:
#             attempts += 1
#             print("太大了")
#         elif num < target:
#             attempts += 1
#             print("太小了")
            
#         else:
#             attempts += 1
#             print(f"猜对了，用了{attempts}次")
#             break
with open("text.txt","r",encoding="utf-8") as f:
    lines = [line.strip().split(",")for line in f if line.strip()]
    scores = []
    for score in lines:
        scores.append(int(score[1]))
    print(scores)