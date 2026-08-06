"""
Day 11 · 前十日综合练习 (2026.8.6)
=====================================
把前 10 天学的所有知识混在一起做。
完成后在终端运行 python Day11_总复习练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 容器选择题（5 分）
# 题目：根据场景选择最合适的容器
#   1. 学生姓名列表，要去重 → 集合
#   2. 一周七天（固定） → 元组
#   3. 学号 → 姓名映射 → 字典
#   4. 购物车（会增删） → 列表
# ============================================================
def problem1():
    a = {"张三","李四","王五"}  # 请修改：存放张三、李四、王五三个学生姓名，且要去重
    b = ("周一","周二","周三","周四","周五","周六","周日")  # 请修改：存放固定不变的一周七天
    c = {"001":"张三","002":"李四"}  # 请修改：用学号001、002映射到张三、李四
    d = ["牛奶","面包"]  # 请修改：存放会增删的购物车，初始有牛奶、面包
    return a, b, c, d


# ============================================================
# 练习 2 · 字符串综合（10 分）
# 题目：清洗并处理一句话
#   输入："  Python is a powerful language  "
#   1. 去掉首尾空格
#   2. 全部转小写
#   3. 按空格拆成单词列表
#   4. 统计单词数
# ============================================================
def problem2():
    text = "  Python is a powerful language  "
    cleaned = text.lower().strip()   # 请修改：strip + lower
    words = cleaned.split()     # 请修改：按空格拆分
    count = len(words)     # 请修改：单词数
    return cleaned, words, count


# ============================================================
# 练习 3 · 字典操作（10 分）
# 题目：给定学生成绩字典
#   1. 用 get 安全获取"王五"的分数（不存在返回 0）
#   2. 获取所有学生的平均分（保留1位）
#   3. 找出分数最高的学生名
# ============================================================
def problem3():
    scores = {"张三": 95, "李四": 82, "王五": 90, "赵六": 76}
    wang_score = scores.get("王五",0)   # 请修改：get 取王五，默认 0
    avg = sum(num for num in scores.values())  / len(scores)        # 请修改：平均分保留1位
    top_student = max(scores.items(),key = lambda x:x[1])[0]  # 请修改：分数最高的学生
    return wang_score, avg, top_student


# ============================================================
# 练习 4 · 集合运算（10 分）
# 题目：两个社团的成员名单
#   1. 同时参加两个社团的人
#   2. 只参加编程社的人
#   3. 所有不重复的人
# ============================================================
def problem4():
    math_club = {"张三", "李四", "王五"}
    coding_club = {"王五", "赵六", "孙七"}
    both = math_club & coding_club      # 请修改：两个都参加
    only_coding = coding_club - both  # 请修改：只参加编程社
    all_members = math_club | coding_club   # 请修改：所有不重复
    return both, only_coding, all_members


# ============================================================
# 练习 5 · 函数 + 异常（10 分）
# 题目：实现 safe_average(scores)
# 正常 → 返回平均分（保留1位）
# 列表为空 → 返回 0（不报错，用 try/except 或 if）
# ============================================================
def safe_average(scores):
    # 请在此处编写代码
    try:
        return round(sum(scores) / len(scores),1)
    except:
        return 0 

# ============================================================
# 练习 6 · 文件读写（10 分）
# 题目：实现 save_and_load(filename, data)
#   1. 把 data（每行一个字符串）写入文件
#   2. 读取文件，返回每行内容列表（去换行符）
# ============================================================
def save_and_load(filename, data):
    # 请在此处编写代码
    with open(filename,"w",encoding="utf-8") as fin:
        for item in data:
            fin.write(item + "\n")
    with open(filename,"r",encoding="utf-8") as fout:
        lines = [line.strip() for line in fout]
    return lines

# ============================================================
# 练习 7 · 推导式 + lambda（10 分）
# 题目：给定学生列表（字典）
#   1. 用推导式提取所有成绩
#   2. 用推导式提取 >= 90 的学生名
#   3. 用 lambda + sorted 按成绩从高到低返回名字列表
# ============================================================
def problem7():
    students = [
        {"name": "张三", "score": 95},
        {"name": "李四", "score": 82},
        {"name": "王五", "score": 90},
        {"name": "赵六", "score": 76},
    ]
    scores = [score["score"] for score in students]       # 请修改：所有成绩列表
    top_names = [name["name"] for name in students if name["score"] >= 90]    # 请修改：>= 90 的姓名
    ranked = [ s["name"] for s in sorted(students,key=lambda x:x["score"],reverse=True)]       # 请修改：按成绩降序的姓名列表
    return scores, top_names, ranked


# ============================================================
# 练习 8 · 综合实战：成绩统计系统（10 分）
# 题目：实现 process_scores(filename)
#   文件内容：姓名,成绩（每行一个学生）
#   返回 (成绩列表, 最高分, 最低分, 平均分保留1位)
#   文件不存在 → 返回 ([], 0, 0, 0)
# ============================================================
def process_scores(filename):
    """
    process_scores("scores.txt") -> ([95, 87, 92], 95, 87, 91.3)
    文件不存在 → ([], 0, 0, 0)
    """
    # 请在此处编写代码
    try:
        with open(filename,"r",encoding="utf-8") as f:
            scores = [int(score.strip().split(",")[1]) for score in f]
        return scores,max(scores),min(scores),sum(scores) / len(scores)
    except FileNotFoundError:
        return [],0,0,0
    
    
        



# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
import os

if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        a, b, c, d = problem1()
        assert a == {"张三", "李四", "王五"}, f"集合: {a}"
        assert b == ("周一", "周二", "周三", "周四", "周五", "周六", "周日"), f"元组: {b}"
        assert c == {"001": "张三", "002": "李四"}, f"字典: {c}"
        assert d == ["牛奶", "面包"], f"列表: {d}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        cleaned, words, count = problem2()
        assert cleaned == "python is a powerful language", f"清洗: {cleaned}"
        assert words == ["python", "is", "a", "powerful", "language"], f"拆分: {words}"
        assert count == 5, f"单词数: {count}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        wang, avg, top = problem3()
        assert wang == 90, f"王五分数: {wang}"
        assert abs(avg - 85.8) < 0.1, f"平均分: {avg}"
        assert top == "张三", f"最高分学生: {top}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        both, only_c, all_m = problem4()
        assert both == {"王五"}, f"共同成员: {both}"
        assert only_c == {"赵六", "孙七"}, f"只编程社: {only_c}"
        assert all_m == {"张三", "李四", "王五", "赵六", "孙七"}, f"所有人: {all_m}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r1 = safe_average([90, 80, 100])
        assert abs(r1 - 90.0) < 0.1, f"平均分: {r1}"
        r2 = safe_average([])
        assert r2 == 0, f"空列表应返回 0: {r2}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        test_file = "_day11_test.txt"
        r = save_and_load(test_file, ["a", "b", "c"])
        assert r == ["a", "b", "c"], f"读写: {r}"
        os.remove(test_file)
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        scores, top_names, ranked = problem7()
        assert scores == [95, 82, 90, 76], f"成绩: {scores}"
        assert top_names == ["张三", "王五"], f">=90: {top_names}"
        assert ranked == ["张三", "王五", "李四", "赵六"], f"排名: {ranked}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        test_file = "_day11_scores.txt"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("张三,95\n李四,87\n王五,92\n")
        r = process_scores(test_file)
        assert r[0] == [95, 87, 92], f"成绩列表: {r[0]}"
        assert r[1] == 95, f"最高分: {r[1]}"
        assert r[2] == 87, f"最低分: {r[2]}"
        assert abs(r[3] - 91.3) < 0.1, f"平均分: {r[3]}"
        r2 = process_scores("_不存在_xyz.txt")
        assert r2 == ([], 0, 0, 0), f"文件不存在: {r2}"
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
        print("  前十日知识掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍总复习知识点再做题。")
    print(f"{'='*40}")
