"""
Day 14 · 数字类型与运算符深挖 练习 (2026.8.9)
====================================
完成后在终端运行 python Day14_数字类型与运算符深挖练习.py 会自动评分。
"""


# ============================================================
# 练习 1 · 判断奇偶（10 分）
# 用位运算判断 n 是否为偶数，是偶数返回 True，否则 False
# 提示：用 n & 1
# ============================================================
def is_even(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 十进制转二进制（10 分）
# 返回 n 的二进制字符串，不要前缀 0b
# 例：to_binary(5) -> "101"
# ============================================================
def to_binary(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 二进制字符串转十进制（10 分）
# 把二进制字符串转成整数
# 例：from_binary("101") -> 5
# 提示：int(s, 2)
# ============================================================
def from_binary(s):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 浮点误差修正（10 分）
# 计算 a + b，并保留 n 位小数返回
# 例：round_float(0.1, 0.2, 2) -> 0.3
# ============================================================
def round_float(a, b, n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 区间判断（10 分）
# 判断 x 是否满足 low < x < high，满足返回 True
# 要求：使用连续比较写法
# ============================================================
def in_range(x, low, high):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · 大数取模（10 分）
# 返回 base 的 exp 次方对 mod 取余的结果
# 例：power_mod(2, 10, 1000) -> 24
# 提示：pow(base, exp, mod)
# ============================================================
def power_mod(base, exp, mod):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 只出现一次的数字（10 分）
# nums 中除了一个数字出现 1 次，其他数字都出现 2 次
# 找出这个唯一的数字，返回它
# 提示：把所有数字异或起来，相同的会抵消
# ============================================================
def single_number(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 交换两个变量（10 分）
# 返回 (b, a)
# 例：swap(3, 5) -> (5, 3)
# 要求：不能直接写 return (b, a) 也行，但要写出两种写法之一
# ============================================================
def swap(a, b):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 9 · 判断 2 的幂（10 分）
# 用位运算判断 n 是否为正的 2 的幂
# 例：8 -> True，10 -> False，1 -> True
# 提示：n > 0 and n & (n - 1) == 0
# ============================================================
def is_power_of_two(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 10 · 二进制位数（10 分）
# 返回 n 的二进制表示一共占几位
# 例：bit_length(1024) -> 11，bit_length(1) -> 1
# 提示：.bit_length()
# ============================================================
def bit_length(n):
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
        assert is_even(4) == True, f"is_even(4): {is_even(4)}"
        assert is_even(7) == False, f"is_even(7): {is_even(7)}"
        assert is_even(0) == True, f"is_even(0): {is_even(0)}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert to_binary(5) == "101", f"to_binary(5): {to_binary(5)}"
        assert to_binary(10) == "1010", f"to_binary(10): {to_binary(10)}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert from_binary("101") == 5, f"from_binary(101): {from_binary('101')}"
        assert from_binary("1111") == 15, f"from_binary(1111): {from_binary('1111')}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert round_float(0.1, 0.2, 2) == 0.3, f"round_float: {round_float(0.1, 0.2, 2)}"
        assert round_float(1.234, 1.111, 2) == 2.35, f"round_float: {round_float(1.234, 1.111, 2)}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert in_range(3, 1, 5) == True, f"in_range(3,1,5): {in_range(3, 1, 5)}"
        assert in_range(5, 1, 5) == False, f"in_range(5,1,5): {in_range(5, 1, 5)}"
        assert in_range(0, 1, 5) == False, f"in_range(0,1,5): {in_range(0, 1, 5)}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert power_mod(2, 10, 1000) == 24, f"power_mod: {power_mod(2, 10, 1000)}"
        assert power_mod(7, 3, 5) == 3, f"power_mod: {power_mod(7, 3, 5)}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert single_number([2, 2, 1]) == 1, f"single_number: {single_number([2, 2, 1])}"
        assert single_number([4, 1, 2, 1, 2]) == 4, f"single_number: {single_number([4, 1, 2, 1, 2])}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert swap(3, 5) == (5, 3), f"swap(3,5): {swap(3, 5)}"
        assert swap(-1, 2) == (2, -1), f"swap(-1,2): {swap(-1, 2)}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        assert is_power_of_two(8) == True, f"is_power_of_two(8): {is_power_of_two(8)}"
        assert is_power_of_two(10) == False, f"is_power_of_two(10): {is_power_of_two(10)}"
        assert is_power_of_two(1) == True, f"is_power_of_two(1): {is_power_of_two(1)}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert bit_length(1024) == 11, f"bit_length(1024): {bit_length(1024)}"
        assert bit_length(1) == 1, f"bit_length(1): {bit_length(1)}"
        assert bit_length(0) == 0, f"bit_length(0): {bit_length(0)}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  数字和运算符掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
