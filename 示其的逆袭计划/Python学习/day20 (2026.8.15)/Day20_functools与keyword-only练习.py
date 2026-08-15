"""
Day 20 · functools 与 keyword-only 练习 (2026.8.15)
====================================
完成后在终端运行 python Day20_functools与keyword-only练习.py 会自动评分。
先看懂 Day20_functools与keyword-only知识点.py 的例题，再做下面的题。
"""

# 本练习会用到这些模块，可以直接使用
import functools


# ============================================================
# 练习 1 · reduce 求和（10 分）
# 用 functools.reduce 实现 sum_list(lst)，返回列表所有数的和
# 例：sum_list([1, 2, 3, 4]) -> 10
# 提示：reduce(lambda a, b: a + b, lst)
# ============================================================
def sum_list(lst):
    # 请在此处编写代码
    return functools.reduce(lambda a, b: a + b, lst)


# ============================================================
# 练习 2 · reduce 连乘（10 分）
# 用 functools.reduce 实现 product(lst)，返回列表所有数的乘积
# 例：product([2, 3, 4]) -> 24
# 提示：reduce(lambda a, b: a * b, lst, 1)，第三个参数是初始值
# ============================================================
def product(lst):
    # 请在此处编写代码
    return functools.reduce(lambda a, b: a * b, lst, 1)


# ============================================================
# 练习 3 · partial 固定指数（10 分）
# 用 functools.partial 实现 square，让 square(n) 返回 n 的平方
# 例：square(3) -> 9, square(10) -> 100
# 提示：square = functools.partial(pow, exp=2)（用关键字固定指数）
# 注意：functools.partial(pow, 2) 固定的是底数，得到的是"2 的 n 次方"
# ============================================================
square = functools.partial(pow, exp=2)


# ============================================================
# 练习 4 · partial 固定进制（10 分）
# 用 functools.partial 实现 bin2int，让 bin2int("1010") -> 10
# 提示：bin2int = functools.partial(int, base=2)
# ============================================================
bin2int = functools.partial(int, base=2)


# ============================================================
# 练习 5 · keyword-only 必填参数（10 分）
# 写 greet(name, *, greeting)，greeting 必须用关键字传且必填
# 例：greet("示其", greeting="早上好") -> "早上好，示其"
# 提示：def greet(name, *, greeting):
# ============================================================
def greet(name, *, greeting):
    # 请在此处编写代码
    return f"{greeting}，{name}"


# ============================================================
# 练习 6 · keyword-only 带默认值（10 分）
# 写 make_sentence(verb, *, obj="Python")，obj 只能用关键字传，默认 "Python"
# 例：make_sentence("学习") -> "学习 Python"
#     make_sentence("学习", obj="数学") -> "学习 数学"
# ============================================================
def make_sentence(verb, *, obj="Python"):
    # 请在此处编写代码
    return f"{verb} {obj}"


# ============================================================
# 练习 7 · lru_cache 优化斐波那契（10 分）
# 给 fib 加上 @functools.lru_cache 装饰器，让 fib(40) 也能秒算
# 例：fib(10) -> 55, fib(50) -> 12586269025
# 提示：在 def fib(n): 上面加 @functools.lru_cache(maxsize=None)
# ============================================================
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# ============================================================
# 练习 8 · lru_cache 统计缓存（10 分）
# 给 climb 加 @functools.lru_cache(maxsize=None)，climb(n) 是爬楼梯走法数
# 例：climb(10) -> 89
# 提示：climb(1)=1, climb(2)=2, climb(n)=climb(n-1)+climb(n-2)
# ============================================================
@functools.lru_cache(maxsize=None)
def climb(n):
    # 请在此处编写代码
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb(n - 1) + climb(n - 2)


# ============================================================
# 练习 9 · cmp_to_key 按长度排序（10 分）
# 写 by_length(a, b)，让 sorted(words, key=functools.cmp_to_key(by_length))
# 按字符串长度升序排序（短的在前）
# 例：["python", "c", "go"] -> ["c", "go", "python"]
# 提示：比较函数返回 len(a) - len(b)
# ============================================================
def by_length(a, b):
    # 请在此处编写代码
    return len(a) - len(b)


# ============================================================
# 练习 10 · cmp_to_key 按个位数排序（10 分）
# 写 by_unit(a, b)，让 sorted(nums, key=functools.cmp_to_key(by_unit))
# 按数字的个位数升序排序
# 例：[23, 41, 12] 的个位数是 3, 1, 2 -> [41, 12, 23]
# 提示：比较函数返回 (a % 10) - (b % 10)
# ============================================================
def by_unit(a, b):
    # 请在此处编写代码
    return (a % 10) - (b % 10)


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        assert sum_list([1, 2, 3, 4]) == 10, f"sum_list: {sum_list([1, 2, 3, 4])}"
        assert sum_list([5, 5, 5]) == 15, f"sum_list: {sum_list([5, 5, 5])}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert product([2, 3, 4]) == 24, f"product: {product([2, 3, 4])}"
        assert product([]) == 1, f"product: {product([])}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert square(3) == 9, f"square: {square(3)}"
        assert square(10) == 100, f"square: {square(10)}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert bin2int("1010") == 10, f"bin2int: {bin2int('1010')}"
        assert bin2int("1111") == 15, f"bin2int: {bin2int('1111')}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert greet("示其", greeting="早上好") == "早上好，示其", f"greet: {greet('示其', greeting='早上好')}"
        assert greet("小明", greeting="你好") == "你好，小明", f"greet: {greet('小明', greeting='你好')}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert make_sentence("学习") == "学习 Python", f"make_sentence: {make_sentence('学习')}"
        assert make_sentence("学习", obj="数学") == "学习 数学", f"make_sentence: {make_sentence('学习', obj='数学')}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert fib(10) == 55, f"fib: {fib(10)}"
        assert fib(50) == 12586269025, f"fib: {fib(50)}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert climb(10) == 89, f"climb: {climb(10)}"
        assert climb(2) == 2, f"climb: {climb(2)}"
        assert climb(1) == 1, f"climb: {climb(1)}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        words = ["python", "c", "go"]
        r9 = sorted(words, key=functools.cmp_to_key(by_length))
        assert r9 == ["c", "go", "python"], f"by_length: {r9}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        nums = [23, 41, 12]
        r10 = sorted(nums, key=functools.cmp_to_key(by_unit))
        assert r10 == [41, 12, 23], f"by_unit: {r10}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  functools 与 keyword-only 掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
