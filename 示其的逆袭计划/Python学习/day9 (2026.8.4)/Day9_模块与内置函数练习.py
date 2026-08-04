"""
Day 9 · 模块与包、常用内置函数 练习 (2026.8.4)
================================================
完成后在终端运行 python Day9_模块与内置函数练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 常用内置函数（5 分）
# 题目：完成以下内置函数的使用
#   1. 把 "123" 转成整数
#   2. 把 3.14159 保留 2 位小数
#   3. 求 -5 的绝对值
#   4. 求 [3, 7, 2, 9] 的最大值
#   5. 判断 3 是否是整数类型（isinstance）
# ============================================================
def problem1():
    a = None  # 请修改：int("123")
    b = None  # 请修改：round(3.14159, 2)
    c = None  # 请修改：abs(-5)
    d = None  # 请修改：max([3, 7, 2, 9])
    e = None  # 请修改：isinstance(3, int)
    return a, b, c, d, e


# ============================================================
# 练习 2 · math 模块（10 分）
# 题目：用 math 模块完成
#   1. 求 81 的平方根
#   2. 求 3.7 向下取整
#   3. 求 2 的 10 次方
#   4. 圆周率 pi 保留 2 位小数
# ============================================================
def problem2():
    import math
    a = None  # 请修改：sqrt(81)
    b = None  # 请修改：floor(3.7)
    c = None  # 请修改：pow(2, 10) 或 2 ** 10
    d = None  # 请修改：round(math.pi, 2)
    return a, b, c, d


# ============================================================
# 练习 3 · random 模块（10 分）
# 题目：用 random 模块完成
#   1. 生成 1~100 之间的随机整数
#   2. 从 ["石头", "剪刀", "布"] 中随机选一个
#   3. 生成一个 0~1 之间的随机小数
# ============================================================
def problem3():
    import random
    a = None  # 请修改：randint(1, 100)
    b = None  # 请修改：choice(["石头", "剪刀", "布"])
    c = None  # 请修改：random()
    return a, b, c


# ============================================================
# 练习 4 · 猜数字游戏（10 分）
# 题目：实现 guess_game()
# 随机生成 1~20 的整数，用户输入数字猜
# 猜大了提示"大了"，猜小了提示"小了"，猜对提示"猜对了"并返回次数
# ============================================================
def guess_game():
    import random
    target = random.randint(1, 20)
    attempts = 0
    # 请在此处编写代码
    
    return attempts


# ============================================================
# 练习 5 · os 模块（10 分）
# 题目：用 os 模块完成
#   1. 获取当前工作目录
#   2. 判断 "data.txt" 是否存在
#   3. 用 os.path.join 拼接 "folder" 和 "file.txt"
# ============================================================
def problem5():
    import os
    a = None  # 请修改：getcwd()
    b = None  # 请修改：path.exists("data.txt")
    c = None  # 请修改：path.join("folder", "file.txt")
    return a, b, c


# ============================================================
# 练习 6 · 创建和使用模块（10 分）
# 题目：在本文件同目录下创建一个 utils.py 文件，
# 里面定义 get_avg(scores) 函数（返回平均分）
# 然后在下面的函数里 import 它并调用
# ============================================================
def problem6():
    # 请先创建 utils.py，然后：
    # import utils
    # 调用 utils.get_avg(...)
    pass


# ============================================================
# 练习 7 · 综合：石头剪刀布（10 分）
# 题目：实现 rps_game(choice)
# 参数 choice 是用户出的（"石头"/"剪刀"/"布"）
# 电脑随机出，返回 (电脑出的, 结果)
# 结果："你赢了" / "你输了" / "平局"
# 规则：石头>剪刀>布>石头
# ============================================================
def rps_game(choice):
    import random
    options = ["石头", "剪刀", "布"]
    computer = random.choice(options)
    # 请在此处编写代码
    
    return computer, result


# ============================================================
# 练习 8 · 综合：模块化成绩系统（10 分）
# 题目：使用 Day 8 的文件操作 + Day 9 的模块化思想
# 实现 load_scores(filename) 读取 CSV 并返回成绩列表
# 返回成绩列表（int 类型）
# ============================================================
def load_scores(filename):
    """
    文件内容：张三,95
    李四,87
    load_scores(filename) -> [95, 87]
    """
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
        a, b, c, d, e = problem1()
        assert a == 123, f"int(123) 应为 123，得到 {a}"
        assert b == 3.14, f"round 应为 3.14，得到 {b}"
        assert c == 5, f"abs(-5) 应为 5，得到 {c}"
        assert d == 9, f"max 应为 9，得到 {d}"
        assert e == True, f"isinstance 应为 True，得到 {e}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        a, b, c, d = problem2()
        assert a == 9.0, f"sqrt(81) 应为 9.0，得到 {a}"
        assert b == 3, f"floor(3.7) 应为 3，得到 {b}"
        assert c == 1024, f"2^10 应为 1024，得到 {c}"
        assert d == 3.14, f"pi 应为 3.14，得到 {d}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        a, b, c = problem3()
        assert 1 <= a <= 100, f"随机整数应在 1~100，得到 {a}"
        assert b in ["石头", "剪刀", "布"], f"随机选择错误: {b}"
        assert 0 <= c <= 1, f"随机小数应在 0~1，得到 {c}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题（需要人工交互，这里直接给分，请自己在终端测试）
    score += 10
    print("[PASS] 第 4 题（请在终端单独测试猜数字游戏）")

    # 第 5 题
    try:
        a, b, c = problem5()
        assert isinstance(a, str) and len(a) > 0, f"getcwd 应为字符串: {a}"
        assert isinstance(b, bool), f"exists 应返回布尔值: {b}"
        assert "folder" in c and "file.txt" in c, f"path.join 错误: {c}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题（需要创建 utils.py，这里检查 import 是否成功）
    try:
        import utils
        assert hasattr(utils, "get_avg"), "utils.py 里应有 get_avg 函数"
        r = utils.get_avg([90, 80, 100])
        assert abs(r - 90.0) < 0.01, f"平均分应为 90，得到 {r}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        for choice in ["石头", "剪刀", "布"]:
            comp, result = rps_game(choice)
            assert comp in ["石头", "剪刀", "布"], f"电脑出招错误: {comp}"
            assert result in ["你赢了", "你输了", "平局"], f"结果错误: {result}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        import os
        test_file = "_day9_test.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("张三,95\n李四,87\n王五,92\n")
        r = load_scores(test_file)
        assert r == [95, 87, 92], f"成绩列表: {r}"
        os.remove(test_file)
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 75")
    print(f"{'='*40}")
    if score >= 60:
        print("  模块与内置函数掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
