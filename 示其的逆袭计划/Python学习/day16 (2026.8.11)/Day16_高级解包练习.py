"""
Day 16 · 高级解包 练习 (2026.8.11)
====================================
完成后在终端运行 python Day16_高级解包练习.py 会自动评分。
"""


# ============================================================
# 练习 1 · 取首尾（10 分）
# 返回 (第一个, 最后一个)
# 例：first_and_last([1, 2, 3, 4, 5]) -> (1, 5)
# 要求：用星号解包：a, *_, b = nums
# ============================================================
def first_and_last(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 取中间部分（10 分）
# 返回去掉首尾后剩下的列表
# 例：middle_values([1, 2, 3, 4, 5]) -> [2, 3, 4]
# 要求：用星号解包：a, *mid, b = nums
# ============================================================
def middle_values(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 头部和剩余（10 分）
# 返回 (第一个, 剩下的列表)
# 例：head_and_rest([10, 20, 30, 40]) -> (10, [20, 30, 40])
# ============================================================
def head_and_rest(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 调用解包（10 分）
# add(a, b, c) 返回三个数的和
# 用调用解包把 nums 拆成三个参数传给 add
# 例：call_add([1, 2, 3]) -> 6
# ============================================================
def add(a, b, c):
    return a + b + c

def call_add(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 字典解包（10 分）
# show(name, age) 返回 f"{name}-{age}"
# 用 ** 把 info 拆成关键字参数传给 show
# 例：call_show({"name": "张三", "age": 18}) -> "张三-18"
# ============================================================
def show(name, age):
    return f"{name}-{age}"

def call_show(info):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · 星号参数拼接（10 分）
# join_words(*words) 把多个单词用空格拼成一个字符串
# 调用时用 * 把列表拆开
# 例：call_join(["Python", "is", "fun"]) -> "Python is fun"
# ============================================================
def join_words(*words):
    # 请在此处编写代码
    pass

def call_join(words):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 矩阵转置（10 分）
# 用 zip(*matrix) 把行变成列
# 例：transpose([[1, 2, 3], [4, 5, 6]]) -> [(1, 4), (2, 5), (3, 6)]
# ============================================================
def transpose(matrix):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 用 ** 合并字典（10 分）
# 返回 {**d1, **d2} 的结果
# 例：merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
#     -> {"a": 1, "b": 3, "c": 4}
# ============================================================
def merge_dicts(d1, d2):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 9 · 嵌套解包（10 分）
# 把 (1, (2, 3)) 解包成三个变量，返回 (a, b, c)
# 例：unpack_nested() -> (1, 2, 3)
# ============================================================
def unpack_nested():
    # 请在此处编写代码
    pass


# ============================================================
# 练习 10 · 解包求和（10 分）
# pairs = [(1, 2), (3, 4), (5, 6)]
# 用 for a, b in pairs 解包，返回每对之和组成的列表
# 例：sum_pairs([(1, 2), (3, 4), (5, 6)]) -> [3, 7, 11]
# ============================================================
def sum_pairs(pairs):
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
        assert first_and_last([1, 2, 3, 4, 5]) == (1, 5), f"first_and_last: {first_and_last([1, 2, 3, 4, 5])}"
        assert first_and_last([7]) == (7, 7), f"first_and_last: {first_and_last([7])}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert middle_values([1, 2, 3, 4, 5]) == [2, 3, 4], f"middle_values: {middle_values([1, 2, 3, 4, 5])}"
        assert middle_values([1, 2, 3]) == [2], f"middle_values: {middle_values([1, 2, 3])}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert head_and_rest([10, 20, 30, 40]) == (10, [20, 30, 40]), f"head_and_rest: {head_and_rest([10, 20, 30, 40])}"
        assert head_and_rest([5]) == (5, []), f"head_and_rest: {head_and_rest([5])}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert call_add([1, 2, 3]) == 6, f"call_add: {call_add([1, 2, 3])}"
        assert call_add([4, 5, 6]) == 15, f"call_add: {call_add([4, 5, 6])}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert call_show({"name": "张三", "age": 18}) == "张三-18", f"call_show: {call_show({'name': '张三', 'age': 18})}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert call_join(["Python", "is", "fun"]) == "Python is fun", f"call_join: {call_join(['Python', 'is', 'fun'])}"
        assert call_join(["a"]) == "a", f"call_join: {call_join(['a'])}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert transpose([[1, 2, 3], [4, 5, 6]]) == [(1, 4), (2, 5), (3, 6)], f"transpose: {transpose([[1, 2, 3], [4, 5, 6]])}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}, f"merge_dicts: {merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        assert unpack_nested() == (1, 2, 3), f"unpack_nested: {unpack_nested()}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert sum_pairs([(1, 2), (3, 4), (5, 6)]) == [3, 7, 11], f"sum_pairs: {sum_pairs([(1, 2), (3, 4), (5, 6)])}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  高级解包掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
