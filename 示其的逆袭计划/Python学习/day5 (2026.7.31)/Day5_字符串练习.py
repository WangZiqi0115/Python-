"""
Day 5 · 字符串方法 练习 (2026.7.31)
======================================
今天学了字符串的各种方法：大小写转换、查找、切割、拼接、替换、格式化。
完成后在终端运行 python Day5_字符串练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 字符串不可变（5 分）
# 题目：给定字符串 s = "python"，执行 s.upper() 后，
# s 的值变了吗？返回 s 的值
# ============================================================
def problem1():
    s = "python"
    s.upper()      # 执行但没接住返回值
    return s       # 返回 s，看看还是不是 "python"


# ============================================================
# 练习 2 · 清洗用户输入（5 分）
# 题目：清洗用户输入：去除首尾空格，全部转小写
# ============================================================
def problem2():
    user_input = "  Zhang San   \n"
    cleaned = None  # 请修改：strip + lower
    return cleaned


# ============================================================
# 练习 3 · 字符串查找（10 分）
# 题目：给定一个文件名字符串，用 find 判断是否包含指定后缀
# 要求：用 find（不是 endswith），不存在返回 "未找到"
# ============================================================
def problem3():
    filename = "report_2024.csv"
    suffix = ".csv"
    
    pos = None   # 请修改：用 find 查找 suffix 的位置
    
    if pos != -1:
        result = f"找到，位置在 {pos}"
    else:
        result = "未找到"
    return result


# ============================================================
# 练习 4 · CSV 解析（10 分）
# 题目：有一行 CSV 数据，先去掉末尾换行符，再按逗号拆分
# 返回拆分后的列表
# ============================================================
def problem4():
    line = "张三,95,重庆,数学学院\n"
    parts = None  # 请修改：strip + split
    return parts  # 应返回 ["张三", "95", "重庆", "数学学院"]


# ============================================================
# 练习 5 · 替换与过滤（10 分）
# 题目：给定一句英文，将其中所有的 "bad" 替换为 "good"
# 并去除首尾空格
# ============================================================
def problem5():
    text = "  this is a bad day, not a bad day  "
    result = None  # 请修改：strip + replace
    return result


# ============================================================
# 练习 6 · 统计单词数（10 分）
# 题目：给定一段英文文本，统计有多少个单词
# 提示：用 split 拆成列表，再数长度
# ============================================================
def problem6():
    text = "Python is a powerful programming language"
    word_count = None  # 请修改
    return word_count


# ============================================================
# 练习 7 · 格式化输出表格（10 分）
# 题目：用 f-string 格式化输出以下表格
# 要求：姓名左对齐宽度10，分数右对齐宽度8，等级居中宽度8
# 不需要 print，返回格式化后的字符串列表
# ============================================================
def problem7():
    data = [
        ("张三", 95, "优秀"),
        ("李四", 87, "良好"),
        ("王五", 60, "及格")
    ]
    result = []
    for name, score, level in data:
        line = None  # 请修改：f-string 格式化
        result.append(line)
    return result
    # 预期：
    # "张三      95   优秀  "
    # "李四      87   良好  "
    # "王五      60   及格  "


# ============================================================
# 练习 8 · 实战：日志分析（10 分）
# 题目：服务器日志每行格式为 "IP地址 - - [时间] 请求方式"
# 请从日志行中提取出 IP 地址和请求方式
# 提示：用 split 按空格拆分，IP 是第一个，请求方式是第6个
# ============================================================
def problem8():
    log_line = '192.168.1.1 - - [31/Jul/2026] "GET /index.html"'
    parts = log_line.split()
    # 请在此处编写代码
    
    ip = None    # 请修改：取 IP（第一个元素）
    method = None  # 请修改：取请求方式（第6个元素），去掉前面的 "
    
    return ip, method


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        r = problem1()
        assert r == "python", f"s 应仍为 \"python\"，得到 {r}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r = problem2()
        assert r == "zhang san", f"预期 'zhang san'，得到 {repr(r)}"
        score += 5
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        r = problem3()
        assert r == "找到，位置在 12", f"预期 '找到，位置在 12'，得到 {r}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        r = problem4()
        assert r == ["张三", "95", "重庆", "数学学院"], f"CSV解析错误: {r}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r = problem5()
        assert r == "this is a good day, not a good day", f"替换错误: {r}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        r = problem6()
        assert r == 6, f"单词数应为 6，得到 {r}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        r = problem7()
        assert len(r) == 3, f"应有 3 行，得到 {len(r)} 行"
        assert "张三" in r[0] and "95" in r[0], f"第一行格式错误: {r[0]}"
        assert "李四" in r[1] and "87" in r[1], f"第二行格式错误: {r[1]}"
        assert "王五" in r[2] and "60" in r[2], f"第三行格式错误: {r[2]}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        ip, method = problem8()
        assert ip == "192.168.1.1", f"IP 应为 192.168.1.1，得到 {ip}"
        assert method == "GET", f"请求方式应为 GET，得到 {method}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 70")
    print(f"{'='*40}")
    if score >= 60:
        print("  字符串方法掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
