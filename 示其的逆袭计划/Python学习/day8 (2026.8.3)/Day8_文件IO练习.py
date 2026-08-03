"""
Day 8 · 文件 I/O + 异常处理 练习 (2026.8.3)
==============================================
完成后在终端运行 python Day8_文件IO练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 写入文件（5 分）
# 题目：把内容列表逐行写入指定文件（每行一个元素）
# 返回读取该文件得到的内容列表
# ============================================================
def write_and_read(filename, lines):
    """
    write_and_read("test.txt", ["a", "b"]) -> ["a", "b"]
    """
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 追加写入（5 分）
# 题目：先写入 ["第一行", "第二行"]，再追加 "第三行"
# 最后读取文件返回所有行
# ============================================================
def append_lines(filename):
    """
    append_lines("test.txt") -> ["第一行", "第二行", "第三行"]
    """
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 安全读取文件（10 分）
# 题目：实现 read_file_safe(filename)
# 文件存在 → 返回内容列表（每行去换行符）
# 文件不存在 → 返回空列表，不崩溃
# ============================================================
def read_file_safe(filename):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 异常处理（10 分）
# 题目：实现 safe_divide(a, b)
# 正常 → 返回 a / b
# b 为 0 → 返回 "不能除以0"
# ============================================================
def safe_divide(a, b):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 异常处理进阶（10 分）
# 题目：实现 parse_number(text)
# 能转成整数 → 返回该整数
# 不能转（如 "abc"）→ 返回 0，不崩溃
# ============================================================
def parse_number(text):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · CSV 文件处理（10 分）
# 题目：有一个 CSV 文件（每行：姓名,成绩），读取后：
#   1. 返回所有学生姓名列表
#   2. 返回成绩平均分（保留一位小数）
# ============================================================
def analyze_csv(filename):
    """
    文件内容：
    张三,95
    李四,87
    王五,92

    analyze_csv(filename) -> (["张三", "李四", "王五"], 91.3)
    """
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 词频统计（10 分）
# 题目：读取文本文件，统计每个单词出现次数（忽略大小写）
# 返回字典
# ============================================================
def word_frequency(filename):
    """
    文件内容：Hello world hello
    word_frequency(filename) -> {"hello": 2, "world": 1}
    """
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 实战：学生成绩写入系统（10 分）
# 题目：实现两个函数
#   1. save_scores(filename, students)：
#      把学生字典 {"姓名": 分数} 写入文件，每行"姓名,分数"
#   2. load_scores(filename)：
#      从文件读取，返回 {"姓名": 分数} 字典
# ============================================================
def save_scores(filename, students):
    """把学生成绩写入文件"""
    # 请在此处编写代码
    pass

def load_scores(filename):
    """从文件读取学生成绩，返回字典"""
    # 请在此处编写代码
    pass


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
import os

if __name__ == "__main__":
    score = 0
    print("=" * 40)
    test_file = "_day8_test.txt"

    # 第 1 题
    try:
        r = write_and_read(test_file, ["a", "b", "c"])
        assert r == ["a", "b", "c"], f"写入读取错误: {r}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r = append_lines(test_file)
        assert r == ["第一行", "第二行", "第三行"], f"追加错误: {r}"
        score += 5
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        r1 = read_file_safe(test_file)
        assert isinstance(r1, list) and len(r1) > 0, f"读取列表错误: {r1}"
        r2 = read_file_safe("_不存在的文件_xyz.txt")
        assert r2 == [], f"文件不存在应返回空列表: {r2}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        r1 = safe_divide(10, 2)
        assert r1 == 5.0, f"10/2 应为 5.0，得到 {r1}"
        r2 = safe_divide(10, 0)
        assert r2 == "不能除以0", f"除0应返回'不能除以0'，得到 {r2}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r1 = parse_number("123")
        assert r1 == 123, f"123 应返回 123，得到 {r1}"
        r2 = parse_number("abc")
        assert r2 == 0, f"abc 应返回 0，得到 {r2}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("张三,95\n李四,87\n王五,92\n")
        names, avg = analyze_csv(test_file)
        assert names == ["张三", "李四", "王五"], f"姓名列表: {names}"
        assert abs(avg - 91.3) < 0.1, f"平均分: {avg}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("Hello world hello Python\n")
        freq = word_frequency(test_file)
        assert freq == {"hello": 2, "world": 1, "python": 1}, f"词频: {freq}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        students = {"张三": 95, "李四": 87}
        save_scores(test_file, students)
        loaded = load_scores(test_file)
        assert loaded == {"张三": 95, "李四": 87}, f"读取成绩: {loaded}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 70")
    print(f"{'='*40}")
    if score >= 60:
        print("  文件操作和异常处理掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
