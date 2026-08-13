"""
Day 18 · 闭包与作用域 练习 (2026.8.13)
====================================
完成后在终端运行 python Day18_闭包与作用域练习.py 会自动评分。
"""


# ============================================================
# 练习 1 · 加法工厂（10 分）
# make_adder(n) 返回一个函数 f(x) = x + n
# 例：make_adder(5)(3) -> 8
# ============================================================
def make_adder(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 乘法工厂（10 分）
# make_multiplier(n) 返回一个函数 f(x) = x * n
# 例：make_multiplier(3)(4) -> 12
# ============================================================
def make_multiplier(n):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 计数器（10 分）
# make_counter() 返回一个函数，每次调用自增 1 并返回
# 例：c = make_counter(); c() -> 1; c() -> 2
# 提示：外层变量 + nonlocal
# ============================================================
def make_counter():
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 问候工厂（10 分）
# make_greeter(name) 返回一个函数 f()，f() 返回 f"你好，{name}"
# 例：make_greeter("张三")() -> "你好，张三"
# ============================================================
def make_greeter(name):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 幂函数工厂（10 分）
# make_power(exp) 返回一个函数 f(base) = base ** exp
# 例：make_power(2)(3) -> 9
# ============================================================
def make_power(exp):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · 累加器（10 分）
# make_accumulator() 返回一个函数 f(value)
# 每次调用把 value 累加到总数，并返回累计结果
# 例：acc = make_accumulator(); acc(1) -> 1; acc(2) -> 3; acc(3) -> 6
# 提示：外层变量 + nonlocal
# ============================================================
def make_accumulator():
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 前缀工厂（10 分）
# make_prefix(prefix) 返回一个函数 f(text) = prefix + text
# 例：make_prefix(">>")("hello") -> ">>hello"
# ============================================================
def make_prefix(prefix):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 修复循环闭包陷阱（10 分）
# create_multipliers() 返回三个函数
# 它们分别应该返回 0、2、4（i * 2，i = 0, 1, 2）
# 要求：用默认参数 i=i 修复
# 例：[f() for f in create_multipliers()] -> [0, 2, 4]
# ============================================================
def create_multipliers():
    funcs = []
    for i in range(3):
        # 请在此处编写代码
        pass
    return funcs


# ============================================================
# 练习 9 · 后缀工厂（10 分）
# make_suffix(suffix) 返回一个函数 f(text) = text + suffix
# 例：make_suffix("!")("hi") -> "hi!"
# ============================================================
def make_suffix(suffix):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 10 · 运算工厂（10 分）
# make_operation(op) 根据 op 返回函数：
#   op == "add"：返回两个数相加的函数
#   op == "mul"：返回两个数相乘的函数
# 例：make_operation("add")(3, 4) -> 7
#     make_operation("mul")(3, 4) -> 12
# ============================================================
def make_operation(op):
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
        assert make_adder(5)(3) == 8, f"make_adder: {make_adder(5)(3)}"
        assert make_adder(10)(1) == 11, f"make_adder: {make_adder(10)(1)}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert make_multiplier(3)(4) == 12, f"make_multiplier: {make_multiplier(3)(4)}"
        assert make_multiplier(2)(5) == 10, f"make_multiplier: {make_multiplier(2)(5)}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        c = make_counter()
        assert c() == 1, f"counter: {c()}"
        assert c() == 2, f"counter: {c()}"
        assert c() == 3, f"counter: {c()}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert make_greeter("张三")() == "你好，张三", f"make_greeter: {make_greeter('张三')()}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert make_power(2)(3) == 9, f"make_power: {make_power(2)(3)}"
        assert make_power(3)(2) == 8, f"make_power: {make_power(3)(2)}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        acc = make_accumulator()
        assert acc(1) == 1, f"accumulator: {acc(1)}"
        assert acc(2) == 3, f"accumulator: {acc(2)}"
        assert acc(3) == 6, f"accumulator: {acc(3)}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert make_prefix(">>")("hello") == ">>hello", f"make_prefix: {make_prefix('>>')('hello')}"
        assert make_prefix("【")("结果") == "【结果", f"make_prefix: {make_prefix('【')('结果')}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert [f() for f in create_multipliers()] == [0, 2, 4], f"create_multipliers: {[f() for f in create_multipliers()]}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        assert make_suffix("!")("hi") == "hi!", f"make_suffix: {make_suffix('!')('hi')}"
        assert make_suffix("分")("95") == "95分", f"make_suffix: {make_suffix('分')('95')}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert make_operation("add")(3, 4) == 7, f"make_operation add: {make_operation('add')(3, 4)}"
        assert make_operation("mul")(3, 4) == 12, f"make_operation mul: {make_operation('mul')(3, 4)}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  闭包与作用域掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
