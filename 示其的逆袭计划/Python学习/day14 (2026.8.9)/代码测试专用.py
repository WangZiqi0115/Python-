# Day 14 · 代码测试专用 (2026.8.9)
# 在这里随便写、随便试，不影响正式练习。

# 示例：试试位运算
# print(5 & 3)
# print(1 << 4)

# # 示例：连续比较
# x = 4
# print(1 < x < 10)

# # 示例：浮点误差 1010 1001       
#                 0010 1000 1001 
# print(0.1 + 0.2)
nums = [11,2,3,2,3,4,4,5,5]
num = nums[0]
for i in range(1,len(nums)):
    num = num^nums[i]
    print(num)
    

