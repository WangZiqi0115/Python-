"""
Day 19 · 装饰器入门 练习 (2026.8.14)
====================================
完成后在终端运行 python Day19_装饰器入门练习.py 会自动评分。
先看懂 Day19_装饰器入门知识点.py 的例题，再做下面的题。
"""

# 本练习会用到这些模块，可以直接使用
import time
import functools
import io
import contextlib


# ============================================================
# 练习 1 · 基础装饰器（10 分）
# my_decorator(func) 返回一个 wrapper，wrapper 调用 func 并原样返回结果
# 例：@my_decorator 装饰后，add(1, 2) -> 3
# ============================================================
def my_decorator(func):
    # 请在此处编写代码
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def add(a,b):
    return a + b


# ============================================================
# 练习 2 · 结果翻倍装饰器（10 分）
# double_result(func) 让被装饰函数的返回值乘以 2
# 例：@double_result 装饰后，add(1, 2) -> 6
# ============================================================
def double_result(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result * 2
    return wrapper
@double_result
def add(a,b):
    return a + b


# ============================================================
# 练习 3 · 结果转大写装饰器（10 分）
# uppercase_result(func) 把字符串返回值变成大写
# 例：@uppercase_result 装饰后，greet("tom") -> "HELLO TOM"
# ============================================================
def uppercase_result(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return str(result).upper()
    return wrapper
@uppercase_result
def greet(name):
    return f"hello,{name}"


# ============================================================
# 练习 4 · 结果加感叹号装饰器（10 分）
# add_exclamation(func) 在字符串返回值后面加 "!"
# 例：@add_exclamation 装饰后，word() -> "hi!"
# ============================================================
def add_exclamation(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return str(result) + "!"
    return wrapper
@add_exclamation
def word(word):
    return word


# ============================================================
# 练习 5 · 结果加中括号装饰器（10 分）
# wrap_result(func) 把返回值用中括号包起来，返回字符串
# 例：@wrap_result 装饰后，num() -> "[5]"
# ============================================================
def wrap_result(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return f"[{result}]"
    return wrapper
@wrap_result
def num(num):
    return num


# ============================================================
# 练习 6 · 调用次数统计装饰器（10 分）
# count_calls(func) 让被装饰函数可以通过 .call_count 查看调用次数
# 例：@count_calls 装饰后，调用 3 次后 f.call_count -> 3
# 提示：给 wrapper 挂一个 call_count 属性，每次调用自增 1
# ============================================================
def count_calls(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        wrapper.call_count += 1
        return func(*args,**kwargs)
    wrapper.call_count = 0
    return wrapper
@count_calls
def add(a,b):
    return a + b



# ============================================================
# 练习 7 · 计时装饰器（10 分）
# time_it(func) 让被装饰函数返回 (结果, 耗时) 元组
# 例：res, cost = add(3, 4)，res -> 7，cost >= 0
# 提示：用 time.perf_counter() 记开始和结束
# ============================================================
def time_it(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        elapsed = end - start
        return result, elapsed
    return wrapper
@time_it
def add(a,b):
    return a + b 


# ============================================================
# 练习 8 · 保留函数名装饰器（10 分）
# keep_name(func) 用 functools.wraps 保留原函数的 __name__
# 例：@keep_name 装饰后，my_add(1, 2) -> 3，my_add.__name__ -> "my_add"
# ============================================================
def keep_name(func):
    # 请在此处编写代码
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        functools.wraps(func)
        return func(*args,**kwargs)
    return wrapper
@keep_name
def my_add(a,b):
    return a + b




# ============================================================
# 练习 9 · 异常兜底装饰器（10 分）
# safe_call(func)：原函数正常就返回结果；抛异常就返回 None
# 例：@safe_call 装饰后，bad() -> None，good() -> 7
# 提示：用 try / except Exception
# ============================================================
def safe_call(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception:
            return None
    return wrapper
@safe_call 
def bad():
    pass
def good():
    pass


# ============================================================
# 练习 10 · 日志装饰器（10 分）
# log_call(func)：调用函数时 print 一条日志，内容里包含函数名，并返回结果
# 例：@log_call 装饰后，add(2, 3) -> 5，同时打印的日志里含有 "add"
# 提示：print(f"调用 {func.__name__} ...")
# ============================================================
def log_call(func):
    # 请在此处编写代码
    def wrapper(*args,**kwargs):
        print(f"调用 {func.__name__} ...")
        return func(*args,**kwargs)
    return wrapper
@log_call
def add(a,b):
    return a + b
    


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        @my_decorator
        def add(a, b):
            return a + b
        assert add(1, 2) == 3, f"my_decorator: {add(1, 2)}"
        assert add(10, 5) == 15, f"my_decorator: {add(10, 5)}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        @double_result
        def add(a, b):
            return a + b
        assert add(1, 2) == 6, f"double_result: {add(1, 2)}"
        assert add(10, 5) == 30, f"double_result: {add(10, 5)}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        @uppercase_result
        def greet(name):
            return f"hello {name}"
        assert greet("tom") == "HELLO TOM", f"uppercase_result: {greet('tom')}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        @add_exclamation
        def word():
            return "hi"
        assert word() == "hi!", f"add_exclamation: {word()}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        @wrap_result
        def num():
            return 5
        assert num() == "[5]", f"wrap_result: {num()}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        @count_calls
        def add(a, b):
            return a + b
        add(1, 2)
        add(3, 4)
        add(5, 6)
        assert add.call_count == 3, f"count_calls: {add.call_count}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        @time_it
        def add(a, b):
            return a + b
        result, elapsed = add(3, 4)
        assert result == 7, f"time_it result: {result}"
        assert elapsed >= 0, f"time_it elapsed: {elapsed}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        @keep_name
        def my_add(a, b):
            return a + b
        assert my_add(1, 2) == 3, f"keep_name: {my_add(1, 2)}"
        assert my_add.__name__ == "my_add", f"keep_name __name__: {my_add.__name__}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        @safe_call
        def good():
            return 7
        @safe_call
        def bad():
            raise ValueError("x")
        assert good() == 7, f"safe_call good: {good()}"
        assert bad() is None, f"safe_call bad: {bad()}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        @log_call
        def add(a, b):
            return a + b
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = add(2, 3)
        assert result == 5, f"log_call result: {result}"
        assert "add" in buf.getvalue(), f"log_call output: {buf.getvalue()!r}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  装饰器入门掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
