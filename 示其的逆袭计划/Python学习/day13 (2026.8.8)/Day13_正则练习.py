"""
Day 13 · 正则表达式 练习 (2026.8.8)
====================================
完成后在终端运行 python Day13_正则练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 提取数字（5 分）
# 用 re.findall 提取文本中的所有数字
# ============================================================
def problem1():
    import re
    text = "我有3个苹果和12个橘子"
    result = None  # 请修改：提取所有数字
    return result


# ============================================================
# 练习 2 · 提取单词（10 分）
# 用 re.findall 提取文本中的所有单词（\w+）
# ============================================================
def problem2():
    import re
    text = "Hello, world! Python is fun."
    result = None  # 请修改：提取所有单词
    return result


# ============================================================
# 练习 3 · 手机号校验（10 分）
# 实现 is_valid_phone(phone)
# 规则：1 开头 + 10 位数字（共 11 位）
# 用 fullmatch，合法返回 True，否则 False
# ============================================================
def is_valid_phone(phone):
    import re
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 邮箱校验（10 分）
# 实现 is_valid_email(email)
# 规则：\w+@\w+\.\w+
# 用 fullmatch
# ============================================================
def is_valid_email(email):
    import re
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 提取日期（10 分）
# 从文本中提取日期，格式：数字-数字-数字（如 2026-08-08）
# 返回第一个匹配（用 search + group）
# ============================================================
def problem5():
    import re
    text = "今天日期是2026-08-08，明天是2026-08-09"
    result = None  # 请修改：提取第一个日期
    return result


# ============================================================
# 练习 6 · 分组提取信息（10 分）
# 从 "姓名 手机号 城市" 格式中提取三部分
# 用 search + 分组
# ============================================================
def problem6():
    import re
    text = "张三 13800138000 重庆"
    # 请在此处编写代码：提取姓名、电话、城市
    
    return name, phone, city


# ============================================================
# 练习 7 · 提取 IP 地址（10 分）
# 从日志行中提取 IP（4 段数字，用 . 分隔）
# ============================================================
def problem7():
    import re
    log = "192.168.1.1 - - [08/Aug/2026] GET /index.html"
    ip = None  # 请修改：提取 IP
    return ip


# ============================================================
# 练习 8 · 实战：解析成绩单（10 分）
# 文本格式："姓名:95 姓名:87 姓名:92"
# 用 findall 提取 (姓名, 分数) 列表
# 计算平均分（保留1位）并返回
# ============================================================
def parse_scores(text):
    """
    parse_scores("张三:95 李四:87 王五:92") -> ([("张三","95"),...], 91.3)
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
        r = problem1()
        assert r == ["3", "12"], f"提取数字: {r}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r = problem2()
        assert r == ["Hello", "world", "Python", "is", "fun"], f"提取单词: {r}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert is_valid_phone("13812345678") == True, "合法手机号应为 True"
        assert is_valid_phone("23812345678") == False, "非1开头应为 False"
        assert is_valid_phone("1381234567") == False, "位数不足应为 False"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert is_valid_email("abc@qq.com") == True, "合法邮箱应为 True"
        assert is_valid_email("abc@qq") == False, "缺域名应为 False"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r = problem5()
        assert r == "2026-08-08", f"日期: {r}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        name, phone, city = problem6()
        assert name == "张三", f"姓名: {name}"
        assert phone == "13800138000", f"电话: {phone}"
        assert city == "重庆", f"城市: {city}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        ip = problem7()
        assert ip == "192.168.1.1", f"IP: {ip}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        pairs, avg = parse_scores("张三:95 李四:87 王五:92")
        assert pairs == [("张三", "95"), ("李四", "87"), ("王五", "92")], f"解析: {pairs}"
        assert abs(avg - 91.3) < 0.1, f"平均分: {avg}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 75")
    print(f"{'='*40}")
    if score >= 60:
        print("  正则基础掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
