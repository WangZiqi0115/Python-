# Python 基础摸底测试
#
# 说明：每个函数对应一道题，函数名和参数已定义好，
# 你只需在 "请在下方编写代码" 的区域内补充实现。
# 运行本文件即可自动评分。
#
# 使用方法：
#   python assessment.py
#
# 共 10 题，每题 10 分，满分 100 分。


# ============================================================
# 第 1 题 · 变量与基本运算（10 分）
# 题目：给定两个整数 a 和 b，返回它们的和、差、积、商（保留两位小数）。
# ============================================================
def problem1(a, b):
    """
    示例：
    problem1(10, 3) -> (13, 7, 30, 3.33)
    """
    # 请在下方编写代码
    c = a + b
    d = a - b
    e = a * b
    f = round(a/b,2)
    return c,d,e,f


# ============================================================
# 第 2 题 · 字符串操作（10 分）
# 题目：给定一个字符串 s，返回翻转后的字符串，以及元音字母('aeiou')的个数。
# 注意：大小写不敏感，即 'A' 和 'a' 都算元音。
# ============================================================
def problem2(s):
    """
    示例：
    problem2("Hello") -> ("olleH", 2)
    """
    # 请在下方编写代码
    count = 0
    s1 = s[::-1]
    for i in s:
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "o" or i == "O" or i == "u" or i =="U":
            count += 1
    return s1,count



# ============================================================
# 第 3 题 · 列表操作（10 分）
# 题目：给定一个整数列表 nums，返回去重后按从大到小排序的新列表。
# ============================================================
def problem3(nums):
    """
    示例：
    problem3([3, 1, 2, 1, 5, 3]) -> [5, 3, 2, 1]
    """
    # 请在下方编写代码
    new_nums = set(nums)
    new_nums2 = list(new_nums)
    new_nums2.sort(reverse=True)
    return new_nums2
a = [1,2,3,2,3,4,5,6,]
print(problem3(a))



# ============================================================
# 第 4 题 · 字典操作（10 分）
# 题目：给定一个字符串 text，统计每个单词出现的次数，返回字典。
# 单词之间以空格分隔，忽略大小写。
# ============================================================
def problem4(text):
    """
    示例：
    problem4("hello world hello") -> {"hello": 2, "world": 1}
    """
    # 请在下方编写代码
    text1 = text.split()
    text2 = {}
    for word in text1:
        if word in text2:
            text2[word] += 1
        else: 
            text2[word] = 1
    return text2
    


# ============================================================
# 第 5 题 · 集合运算（10 分）
# 题目：给定两个整数列表 list1 和 list2，返回它们的交集（升序列表）。
# ============================================================
def problem5(list1, list2):
    """
    示例：
    problem5([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
    """
    # 请在下方编写代码
    s1 = set(list1)
    s2 = set(list2)
    s3 = s1|s2
    list3 = list(s3)
    list3.sort()
    return list3


# ============================================================
# 第 6 题 · 条件与循环（10 分）
# 题目：打印出 100 到 999 之间所有的"水仙花数"并返回列表。
# 水仙花数：各位数字的立方和等于该数本身，如 153 = 1^3 + 5^3 + 3^3。
# ============================================================
def problem6():
    """
    示例：
    problem6() -> [153, 370, 371, 407]
    """
    # 请在下方编写代码
    lst = []
    for i in range(100,1000):
        b = i%10        #取个位数
        c = i%100//10   #取十位数
        d = i//100      #取百位数
        if i == b ** 3 + c ** 3 + d ** 3:
            lst.append(i)
    return lst


# ============================================================
# 第 7 题 · 函数进阶（10 分）
 # 题目：实现一个函数 make_multiplier(n)，它返回一个新的函数。
 # 这个新函数接收一个数字 x，返回 n * x 的结果。
# ============================================================
def make_multiplier(n):

    # 请在下方编写代码
    def new_multiplier(x):
        return n*x
    return new_multiplier

 
 
# ============================================================
# 第 8 题 · 列表推导式（10 分）
# 题目：给定一个整数列表 nums，用列表推导式返回所有偶数的平方组成的列表。
# ============================================================
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


# ============================================================
# 第 9 题 · 文件与异常处理（10 分）
# 题目：给定文件名 filename 和内容列表 lines，
# 将 lines 逐行写入文件（每行一个元素），然后读取该文件返回内容列表。
# 注意处理文件可能存在的异常。
# ============================================================
def problem9(filename, lines):
    """
    示例：
    problem9("test.txt", ["a", "b", "c"]) -> ["a", "b", "c"]
    """
    # 请在下方编写代码
    pass


# ============================================================
# 第 10 题 · 综合应用（10 分）
# 题目：实现一个简单的**学生成绩管理系统**（函数内实现即可）：
#   用一个字典存储学生信息，key 为学号，value 为姓名和成绩的字典。
#   实现以下三个功能（函数内部定义嵌套函数）：
#     - add_student(sid, name, score): 添加学生
#     - get_student(sid): 查询学生信息，返回 (name, score) 或 None
#     - get_top(n): 返回成绩最高的前 n 个学生的 (name, score) 列表
#   示例见下方。
# ============================================================
def problem10():
    """
    示例流程：
    mgr = problem10()
    mgr["add"]("001", "Alice", 95)
    mgr["add"]("002", "Bob", 87)
    mgr["get"]("001")  -> ("Alice", 95)
    mgr["top"](2)      -> [("Alice", 95), ("Bob", 87)]
    """
    students = {}

    def add_student(sid, name, score):
        # 请在下方编写代码
        pass

    def get_student(sid):
        # 请在下方编写代码
        pass

    def get_top(n):
        # 请在下方编写代码
        pass

    return {"add": add_student, "get": get_student, "top": get_top}


# ============================================================
# 以下为测试运行代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    total = 100

    # 第 1 题
    try:
        r1 = problem1(10, 3)
        assert r1 == (13, 7, 30, 3.33), f"预期 (13, 7, 30, 3.33)，得到 {r1}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r2 = problem2("Hello")
        assert r2 == ("olleH", 2), f"预期 ('olleH', 2)，得到 {r2}"
        r2b = problem2("AEIOU")
        assert r2b == ("UOIEA", 5), f"全元音测试失败，得到 {r2b}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        r3 = problem3([3, 1, 2, 1, 5, 3])
        assert r3 == [5, 3, 2, 1], f"预期 [5, 3, 2, 1]，得到 {r3}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        r4 = problem4("hello world hello")
        assert r4 == {"hello": 2, "world": 1}, f"预期 {{'hello': 2, 'world': 1}}，得到 {r4}"
        r4b = problem4("Hello HELLO hello")
        assert r4b == {"hello": 3}, f"忽略大小写测试失败，得到 {r4b}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r5 = problem5([1, 2, 3, 4], [3, 4, 5, 6])
        assert r5 == [3, 4], f"预期 [3, 4]，得到 {r5}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        r6 = problem6()
        assert r6 == [153, 370, 371, 407], f"预期 [153, 370, 371, 407]，得到 {r6}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        from assessment import make_multiplier
        double = make_multiplier(2)
        assert double(5) == 10, f"double(5) 预期 10，得到 {double(5)}"
        triple = make_multiplier(3)
        assert triple(4) == 12, f"triple(4) 预期 12，得到 {triple(4)}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        r8 = problem8([1, 2, 3, 4, 5, 6])
        assert r8 == [4, 16, 36], f"预期 [4, 16, 36]，得到 {r8}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        import os
        test_file = "_test_temp.txt"
        r9 = problem9(test_file, ["a", "b", "c"])
        assert r9 == ["a", "b", "c"], f"预期 ['a', 'b', 'c']，得到 {r9}"
        if os.path.exists(test_file):
            os.remove(test_file)
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        mgr = problem10()
        mgr["add"]("001", "Alice", 95)
        mgr["add"]("002", "Bob", 87)
        mgr["add"]("003", "Charlie", 92)
        assert mgr["get"]("001") == ("Alice", 95), f"get 测试失败，得到 {mgr['get']('001')}"
        assert mgr["get"]("999") is None, f"不存在的学生应返回 None"
        top2 = mgr["top"](2)
        assert top2 == [("Alice", 95), ("Charlie", 92)], f"top(2) 预期 [('Alice',95),('Charlie',92)]，得到 {top2}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 输出总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / {total}")
    print(f"{'='*40}")
    if score == total:
        print("  太强了！你已经基本掌握了 Python 基础语法！")
    elif score >= 80:
        print("  基础很扎实！还有少数需要补强的知识点。")
    elif score >= 60:
        print("  核心语法基本掌握，部分内容需要巩固。")
    elif score >= 40:
        print("  基础比较薄弱，建议从基础语法重新梳理。")
    else:
        print("  大部分还未掌握，需要系统学习基础内容。")
    print(f"{'='*40}")
# *** End File
