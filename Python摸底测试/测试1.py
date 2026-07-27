# def problem3(nums):
#     """
#     示例：
#     problem3([3, 1, 2, 1, 5, 3]) -> [5, 3, 2, 1]
#     """
#     # 请在下方编写代码
#     new_nums = set(nums)
#     new_nums2 = list(new_nums)
#     new_nums2.sort(reverse=True)
#     return new_nums2
# a = [1,2,3,2,3,4,5,6,]
# print(problem3(a))
# def problem4(text):
#     """
#     示例：
#     problem4("hello world hello") -> {"hello": 2, "world": 1}
#     """
#     # 请在下方编写代码
#     new_text = text.split()
#     return new_text
# s = "hello python world"
# s1 = problem4(s)
# print(s1)
# def problem4(text):
#     """
#     示例：
#     problem4("hello world hello") -> {"hello": 2, "world": 1}
#     """
#     # 请在下方编写代码
#     text1 = text.split()
#     text2 = {}
#     for word in text1:
#         if word in text2:
#             text2[word] += 1
#         else: 
#             text2[word] = 1
#     return text2
# s = "hello world hello"
# s1 = problem4(s)
# print(s1)
# s = {1,2,3,4,4,5}
# print(s)
# def problem5(list1, list2):
#     """
#     示例：
#     problem5([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
#     """
#     # 请在下方编写代码
#     s1 = set(list1)
#     s2 = set(list2)
#     s3 = s1|s2
#     list3 = list(s3)
#     list3.sort()
#     return list3


# lst = []
# for i in range(100,1000):
#     b = i%10        #取个位数
#     c = i%100//10   #取十位数
#     d = i//100      #取百位数
#     if i == b ** 3 + c ** 3 + d ** 3:
#         lst.append(i)
# print(lst)
# def make_multiplier(n):
#     """
#     示例：
#     double = make_multiplier(2)
#     double(5) -> 10

#     triple = make_multiplier(3)
#     triple(4) -> 12
#     """
#     # 请在下方编写代码
#     def new_multiplier(x):
#         return n*x
#     return new_multiplier

# double = make_multiplier(2)
# print(double(5))
def problem8(nums):
    """
    示例：
    problem8([1, 2, 3, 4, 5, 6]) -> [4, 16, 36]
    """
    # 请在下方编写代码
    new_lst = []
    for i in nums:
        if i % 2 == 0:
            num = i**2
            new_lst.append(num)
    return new_lst
s = [1,2,34,4,5,]
print(problem8(s))

