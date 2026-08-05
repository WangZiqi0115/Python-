"""
Day 10 · 推导式 / 生成器 / lambda 进阶 练习 (2026.8.5)
=========================================================
完成后在终端运行 python Day10_推导式生成器lambda练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 列表推导式（5 分）
# 题目：用一行列表推导式完成
#   1. 生成 1~10 的平方列表
#   2. 生成 1~20 中偶数的列表
#   3. 把 ["a", "b", "c"] 转成大写
# ============================================================
def problem1():
    a = [num ** 2 for num in range(1,11)]  # 请修改：1~10 的平方
    b = [num for num in range(1,21) if num % 2 == 0] # 请修改：1~20 的偶数
    c = [letter.upper() for letter in ["a", "b", "c"]]  # 请修改：["a", "b", "c"] 转大写
    return a, b, c


# ============================================================
# 练习 2 · 推导式 + 条件（10 分）
# 题目：
#   1. 用推导式生成 1~30 中能被 3 整除的数（过滤）
#   2. 用推导式生成 1~10 的"偶"/"奇"标记列表（选值）
# ============================================================
def problem2():
    a = [num for num in range(1,31) if num % 3 == 0]  # 请修改：1~30 能被 3 整除
    b = ["奇" if num % 2 == 1 else "偶" for num in range(1,11)]  # 请修改：["偶", "奇", "偶", ...] 1~10
    return a, b


# ============================================================
# 练习 3 · 嵌套推导式（10 分）
# 题目：
#   1. 把二维列表 [[1,2],[3,4],[5,6]] 扁平化
#   2. 生成 0~2 的所有坐标对 [(0,0),(0,1),...]
# ============================================================
def problem3():
    matrix = [[1, 2], [3, 4], [5, 6]]
    a = [num for row in matrix for num in row]  # 请修改：扁平化 matrix
    b = [(x,y) for x in range(0,3) for y in range(0,3)]  # 请修改：0~2 的所有坐标对
    return a, b


# ============================================================
# 练习 4 · lambda 基础（10 分）
# 题目：
#   1. 用 lambda 定义"乘以 3"的函数并调用
#   2. 用 lambda 定义"两个数相加"的函数并调用
#   3. 用 lambda 作为 sorted 的 key 按分数排序学生
# ============================================================
def problem4():
    triple = lambda x:x * 3   # 请修改：lambda 乘以 3
    add_two = lambda a,b:a+b  # 请修改：lambda 两个数相加
    students = [("张三", 82), ("李四", 95), ("王五", 90)]
    ranked = sorted(students,key = lambda x:x[1],reverse=True)   # 请修改：按分数从高到低
    
    return triple(5), add_two(3, 7), ranked


# ============================================================
# 练习 5 · 生成器（10 分）
# 题目：
#   1. 用生成器表达式生成 1~10 的平方生成器，转成列表
#   2. 用 sum 配合生成器求 1~100 所有整数的和
#   3. 验证生成器用两次后第二次是空的
# ============================================================
def problem5():
    a = list(x ** 2 for x in range(1,11))  # 请修改：1~10 平方的生成器 → 转列表
    b = sum(x for x in range(1,101))  # 请修改：sum(生成器) 求 1~100 的和
    gen = (x for x in [1, 2, 3])
    first = list(gen)
    second = list(gen)
    return a, b, first, second


# ============================================================
# 练习 6 · 字典推导式（10 分）
# 题目：
#   1. 生成 {1:1, 2:4, 3:9, ...} 1~5 的平方字典
#   2. 把 {"a":1, "b":2} 反转成 {1:"a", 2:"b"}
#   3. 用推导式生成 1~10 中偶数的立方字典 {2:8, 4:64, ...}
# ============================================================
def problem6():
    a = {x:x ** 2 for x in range(1,6)}  # 请修改：1~5 平方字典
    d = {"a": 1, "b": 2}
    b = {k:v for v,k in d.items()}  # 请修改：反转字典
    c = {x:x ** 3 for x in range(1,11) if x % 2 == 0}  # 请修改：偶数立方字典
    return a, b, c


# ============================================================
# 练习 7 · 综合：数据处理（10 分）
# 题目：有一份学生成绩数据（列表套字典）
#   1. 提取所有学生姓名
#   2. 提取成绩 >= 90 的学生姓名
#   3. 计算所有学生平均分
#   4. 按成绩从高到低排序，返回名字列表
# ============================================================
def problem7():
    students = [
        {"name": "张三", "score": 95},
        {"name": "李四", "score": 82},
        {"name": "王五", "score": 90},
        {"name": "赵六", "score": 76},
    ]
    names = [name["name"] for name in students]        # 请修改：所有姓名
    top_names = [name["name"] for name in students if name["score"] >= 90 ]    # 请修改：>= 90 的姓名
    avg = round(sum(score["score"] for score in students) / len(students))         # 请修改：平均分（保留1位）
    ranked = [name["name"] for name in sorted(students,key= lambda x:x["score"],reverse=True)]       # 请修改：按成绩从高到低的姓名列表
    
    return names, top_names, avg, ranked


# ============================================================
# 练习 8 · 实战：数据清洗管道（10 分）
# 题目：有一份原始数据列表，包含空值、多余空格、数字字符串
#   1. 去掉空值
#   2. 去除首尾空格
#   3. 把数字字符串转成 int
# 返回清洗后的列表
# ============================================================
def clean_data(raw_data):
    """
    clean_data([" 95 ", "", " 87", "92 ", "  "]) -> [95, 87, 92]
    """
    # 请在此处编写代码
    lines =[int(num.strip()) for num in raw_data if num.strip()]
    return lines


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        a, b, c = problem1()
        assert a == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], f"平方列表: {a}"
        assert b == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], f"偶数列表: {b}"
        assert c == ["A", "B", "C"], f"大写列表: {c}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        a, b = problem2()
        assert a == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], f"被3整除: {a}"
        assert b == ["奇", "偶", "奇", "偶", "奇", "偶", "奇", "偶", "奇", "偶"], f"奇偶标记: {b}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        a, b = problem3()
        assert a == [1, 2, 3, 4, 5, 6], f"扁平化: {a}"
        assert b == [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], f"坐标对: {b}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        t, s, ranked = problem4()
        assert t == 15, f"triple(5) 应为 15，得到 {t}"
        assert s == 10, f"add(3,7) 应为 10，得到 {s}"
        assert ranked == [("李四", 95), ("王五", 90), ("张三", 82)], f"排序: {ranked}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        a, b, first, second = problem5()
        assert a == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], f"生成器转列表: {a}"
        assert b == 5050, f"1~100 和应为 5050，得到 {b}"
        assert first == [1, 2, 3], f"第一次: {first}"
        assert second == [], f"第二次应为空: {second}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        a, b, c = problem6()
        assert a == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, f"平方字典: {a}"
        assert b == {1: "a", 2: "b"}, f"反转: {b}"
        assert c == {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}, f"立方字典: {c}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        names, top, avg, ranked = problem7()
        assert names == ["张三", "李四", "王五", "赵六"], f"姓名: {names}"
        assert top == ["张三", "王五"], f">=90: {top}"
        assert abs(avg - 85.8) < 0.1, f"平均分: {avg}"
        assert ranked == ["张三", "王五", "李四", "赵六"], f"排名: {ranked}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        r = clean_data([" 95 ", "", " 87", "92 ", "  "])
        assert r == [95, 87, 92], f"清洗结果: {r}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 75")
    print(f"{'='*40}")
    if score >= 60:
        print("  推导式与 lambda 掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
