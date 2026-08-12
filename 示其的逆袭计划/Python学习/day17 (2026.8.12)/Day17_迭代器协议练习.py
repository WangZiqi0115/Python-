"""
Day 17 · 迭代器协议 练习 (2026.8.12)
====================================
完成后在终端运行 python Day17_迭代器协议练习.py 会自动评分。
"""


# ============================================================
# 练习 1 · 手动取第一个（10 分）
# 用 iter + next 返回 nums 的第一个元素，不要用 nums[0]
# 例：first_element([10, 20, 30]) -> 10
# ============================================================
def first_element(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 手动取前两个（10 分）
# 用 iter + next 返回前两个元素组成的元组
# 例：first_two([1, 2, 3]) -> (1, 2)
# ============================================================
def first_two(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 安全的 next（10 分）
# 对迭代器 it 取下一个元素
# 有就返回元素，没有就返回 None
# 例：next_or_none(iter([5])) -> 5
# ============================================================
def next_or_none(it):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 判断是否可迭代（10 分）
# 用 iter() 判断 obj 是否可迭代
# 能 iter() 返回 True，不能返回 False
# 例：is_iterable([1, 2]) -> True，is_iterable(5) -> False
# 提示：iter(obj) 对不可迭代对象会抛 TypeError
# ============================================================
def is_iterable(obj):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 手动模拟 for 循环（10 分）
# 用 iter + next + while + StopIteration
# 把 nums 的所有元素收集成列表返回
# 例：iterate_all([1, 2, 3]) -> [1, 2, 3]
# ============================================================
def iterate_all(nums):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · 取前 n 个（10 分）
# 用 iter + next 取 nums 的前 n 个元素，返回列表
# 例：take_n([10, 20, 30, 40], 2) -> [10, 20]
# ============================================================
def take_n(nums, n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 倒计时列表（10 分）
# 返回 [n, n-1, ..., 1]
# 例：countdown_list(3) -> [3, 2, 1]
# 提示：可以自定义 Countdown 类（参考知识点），也可以 while 实现
# ============================================================
def countdown_list(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 字典键列表（10 分）
# 返回字典所有键组成的列表
# 例：dict_keys_list({"a": 1, "b": 2}) -> ["a", "b"]
# 提示：可以用 iter(d) 或直接 list(d)
# ============================================================
def dict_keys_list(d):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 9 · 迭代器只能用一次（10 分）
# consume_once(iterator) 返回 list(iterator)
# 同一个迭代器传两次，第二次应该得到 []
# ============================================================
def consume_once(iterator):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 10 · 生成器倒计时（10 分）
# 用 yield 写一个生成器函数，产生 n, n-1, ..., 1
# 例：list(gen_countdown(3)) -> [3, 2, 1]
# ============================================================
def gen_countdown(n):
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
        assert first_element([10, 20, 30]) == 10, f"first_element: {first_element([10, 20, 30])}"
        assert first_element([7]) == 7, f"first_element: {first_element([7])}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert first_two([1, 2, 3]) == (1, 2), f"first_two: {first_two([1, 2, 3])}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        it = iter([5, 6])
        assert next_or_none(it) == 5, f"next_or_none: {next_or_none(it)}"
        assert next_or_none(it) == 6, f"next_or_none: {next_or_none(it)}"
        assert next_or_none(it) is None, f"next_or_none: {next_or_none(it)}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert is_iterable([1, 2]) == True, f"is_iterable: {is_iterable([1, 2])}"
        assert is_iterable(5) == False, f"is_iterable: {is_iterable(5)}"
        assert is_iterable("abc") == True, f"is_iterable: {is_iterable('abc')}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert iterate_all([1, 2, 3]) == [1, 2, 3], f"iterate_all: {iterate_all([1, 2, 3])}"
        assert iterate_all([]) == [], f"iterate_all: {iterate_all([])}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert take_n([10, 20, 30, 40], 2) == [10, 20], f"take_n: {take_n([10, 20, 30, 40], 2)}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert countdown_list(3) == [3, 2, 1], f"countdown_list: {countdown_list(3)}"
        assert countdown_list(1) == [1], f"countdown_list: {countdown_list(1)}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert dict_keys_list({"a": 1, "b": 2}) == ["a", "b"], f"dict_keys_list: {dict_keys_list({'a': 1, 'b': 2})}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        it = iter([1, 2, 3])
        assert consume_once(it) == [1, 2, 3], f"consume_once: {consume_once(it)}"
        assert consume_once(it) == [], f"第二次应为空: {consume_once(it)}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert list(gen_countdown(3)) == [3, 2, 1], f"gen_countdown: {list(gen_countdown(3))}"
        assert list(gen_countdown(1)) == [1], f"gen_countdown: {list(gen_countdown(1))}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  迭代器协议掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
