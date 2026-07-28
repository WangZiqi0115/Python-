"""
Day 3 · Dict 字典 练习
=========================
今天学了字典的创建、取值、增删改、遍历、推导式。
完成后在终端运行 python Day3_Dict练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 创建字典（5 分）
# 题目：按要求创建以下字典
#   1. 创建字典 d1，包含 name: "示其", age: 18, major: "数学"
#   2. 创建空字典 d2
#   3. 用 dict() 创建 d3：name="张三", score=95
# ============================================================
def problem1():
    d1 = None  # 请修改
    d2 = None  # 请修改
    d3 = None  # 请修改
    return d1, d2, d3


# ============================================================
# 练习 2 · 字典取值（5 分）
# 题目：给定一个学生字典，用两种方式取出 age
# 要求：a 用方括号，b 用 get，c 用 get 取不存在的 key 并给默认值 0
# ============================================================
def problem2():
    student = {"name": "示其", "age": 18, "score": 92}
    a = None  # 请修改：用方括号取 age
    b = None  # 请修改：用 get 取 age
    c = None  # 请修改：用 get 取 "height"，默认值 0
    return a, b, c


# ============================================================
# 练习 3 · 字典增删改（10 分）
# 题目：对字典 d = {"a": 1, "b": 2} 依次操作
#   1. 添加 "c": 3
#   2. 把 "b" 的值改为 99
#   3. 删除 "a"
#   4. 添加 "d": 4
#   5. 用 update 合并 {"e": 5, "f": 6}
# ============================================================
def problem3():
    d = {"a": 1, "b": 2}
    # 请在此处编写代码
    
    return d   # 应该返回 {"b": 99, "c": 3, "d": 4, "e": 5, "f": 6}


# ============================================================
# 练习 4 · 遍历字典（10 分）
# 题目：给定一个成绩字典，打印出每位学生的名字和成绩，
# 格式：张三: 95分
# 计算并返回平均分（保留一位小数）
# ============================================================
def problem4():
    scores = {"张三": 95, "李四": 87, "王五": 92, "赵六": 78}
    
    total = 0
    count = 0
    # 请在此处编写代码：遍历并打印
    
    avg = None  # 请修改：计算平均分
    return avg   # 返回平均分


# ============================================================
# 练习 5 · 词频统计（10 分）
# 题目：给定一段英文文本，统计每个单词出现的次数
# 要求：忽略大小写（"Hello" 和 "hello" 算同一个词）
# 用 get() 实现，不要用 if in
# ============================================================
def problem5():
    text = "Hello world hello Python world hello"
    freq = {}
    # 请在此处编写代码
    
    return freq  # 应返回 {"hello": 3, "world": 2, "python": 1}


# ============================================================
# 练习 6 · 字典推导式（10 分）
# 题目：给定一个列表 nums，用字典推导式生成一个字典
# key 为数字，value 为该数字的立方
# 只处理偶数
# ============================================================
def problem6():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 请在此处编写代码（一行字典推导式）
    
    return None  # 请修改


# ============================================================
# 练习 7 · 反转字典（10 分）
# 题目：给定一个字典 d，返回一个反转后的新字典
# 原 value 变成新 key，原 key 变成新 value
# 提示：用字典推导式 + items()
# ============================================================
def problem7():
    d = {"a": 1, "b": 2, "c": 3}
    # 请在此处编写代码
    
    return None  # 请修改，应返回 {1: "a", 2: "b", 3: "c"}


# ============================================================
# 练习 8 · 实战：学生信息管理（10 分）
# 题目：用字典实现一个简单的学生管理系统
# 已有数据是一个字典，key 为学号，value 为姓名
# 实现以下两个函数：
#   add_student(students, sid, name): 添加学生，返回新字典
#   get_name(students, sid): 根据学号查姓名，不存在返回 "未知"
# ============================================================
students = {
    "001": "张三",
    "002": "李四",
    "003": "王五"
}

def add_student(students, sid, name):
    """添加学生，返回新字典"""
    # 请在此处编写代码
    pass

def get_name(students, sid):
    """根据学号查姓名，不存在返回"未知" """
    # 请在此处编写代码
    pass


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        d1, d2, d3 = problem1()
        assert d1 == {"name": "示其", "age": 18, "major": "数学"}, f"d1 错误: {d1}"
        assert d2 == {}, f"d2 应为空字典: {d2}"
        assert d3 == {"name": "张三", "score": 95}, f"d3 错误: {d3}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        a, b, c = problem2()
        assert a == 18, f"方括号取 age 应为 18，得到 {a}"
        assert b == 18, f"get 取 age 应为 18，得到 {b}"
        assert c == 0, f"不存在的 key 默认值应为 0，得到 {c}"
        score += 5
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        result = problem3()
        expected = {"b": 99, "c": 3, "d": 4, "e": 5, "f": 6}
        assert result == expected, f"预期 {expected}，得到 {result}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        avg = problem4()
        assert abs(avg - 88.0) < 0.1, f"平均分应为 88.0，得到 {avg}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        freq = problem5()
        assert freq == {"hello": 3, "world": 2, "python": 1}, f"词频错误: {freq}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        result = problem6()
        expected = {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
        assert result == expected, f"预期 {expected}，得到 {result}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        result = problem7()
        assert result == {1: "a", 2: "b", 3: "c"}, f"反转错误: {result}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        s = {"001": "张三"}
        s = add_student(s, "002", "李四")
        assert s == {"001": "张三", "002": "李四"}, f"添加后: {s}"
        name = get_name(s, "001")
        assert name == "张三", f"查001应为张三，得到 {name}"
        name = get_name(s, "999")
        assert name == "未知", f"查不存在的学号应为'未知'，得到 {name}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 70")
    print(f"{'='*40}")
    if score >= 60:
        print("  字典掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
