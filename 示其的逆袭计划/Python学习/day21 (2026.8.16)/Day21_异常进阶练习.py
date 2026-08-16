"""
Day 21 · 异常进阶 练习 (2026.8.16)
====================================
完成后在终端运行 python Day21_异常进阶练习.py 会自动评分。
先看懂 Day21_异常进阶知识点.py 的例题，再做下面的题。
"""


# ============================================================
# 练习 1 · 除零兜底（10 分）
# safe_divide(a, b)：a 除以 b，正常返回结果；除零时返回 None
# 例：safe_divide(10, 2) -> 5.0, safe_divide(1, 0) -> None
# 提示：try / except ZeroDivisionError
# ============================================================
def safe_divide(a, b):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 2 · else 只在成功时执行（10 分）
# divide_with_else(a, b)：正常时返回结果并 print("计算成功")；除零返回 None
# 例：divide_with_else(10, 2) -> 5.0 且打印"计算成功"；divide_with_else(1, 0) -> None
# 提示：try / except / else（else 只在没出错时执行）
# ============================================================
def divide_with_else(a, b):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 3 · 转换兜底（10 分）
# read_int(text)：把字符串转成整数，成功返回数字；转不了返回 None
# 例：read_int("42") -> 42, read_int("abc") -> None, read_int(None) -> None
# 提示：except (ValueError, TypeError)
# ============================================================
def read_int(text):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 4 · 主动抛异常（10 分）
# validate_age(age)：年龄在 0~150 之间返回 "年龄有效"；否则 raise ValueError
# 例：validate_age(25) -> "年龄有效"；validate_age(-1) 抛 ValueError
# 提示：raise ValueError（带提示信息）
# ============================================================
def validate_age(age):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 5 · 分数校验（10 分）
# check_score(score)：0~100 之间返回 "合格"；否则 raise ValueError
# 例：check_score(85) -> "合格"；check_score(150) 抛 ValueError
# 提示：raise ValueError（带提示信息）
# ============================================================
def check_score(score):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 6 · assert 断言（10 分）
# check_positive(x)：用 assert 检查 x > 0，成立返回 "是正数"；不成立抛 AssertionError
# 例：check_positive(5) -> "是正数"；check_positive(-1) 抛 AssertionError
# 提示：assert
# ============================================================
def check_positive(x):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 7 · 自定义异常（10 分）
# 自定义异常类 MyError（必须继承 Exception）
# process(ok)：ok 为 True 返回 "OK"；ok 为 False 时 raise MyError
# 例：process(True) -> "OK"；process(False) 抛 MyError
# 提示：class MyError(Exception) + raise MyError（带提示信息）
# ============================================================
class MyError:
    # 请在此处编写代码（提示：继承 Exception）
    pass


def process(ok):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 8 · 异常链（10 分）
# inner()：主动抛 ValueError("内部错误")
# outer()：调用 inner()，捕获后抛 RuntimeError，并用 from 保留原始原因
# 例：outer() 会抛 RuntimeError，且 e.__cause__ 是 ValueError
# 提示：raise ... from ...（异常链）
# ============================================================
def inner():
    # 请在此处编写代码
    return None


def outer():
    # 请在此处编写代码
    return None


# ============================================================
# 练习 9 · finally 收尾（10 分）
# safe_open(filename)：读取文件返回内容；文件不存在返回 None；
# 无论成功失败，最后都要 print("已结束")（用 finally）
# 例：safe_open("存在的.txt") -> 文件内容；safe_open("不存在的.txt") -> None
# 提示：with open + except OSError + finally
# ============================================================
def safe_open(filename):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 10 · 综合：自定义异常 + 转换（10 分）
# 自定义异常类 NumberError（必须继承 Exception）
# parse(text)：把字符串转整数，成功返回数字；转不了抛 NumberError（不是 ValueError）
# 例：parse("42") -> 42；parse("abc") 抛 NumberError
# 提示：class NumberError(Exception) + try/except + raise
# ============================================================
class NumberError:
    # 请在此处编写代码（提示：继承 Exception）
    pass


def parse(text):
    # 请在此处编写代码
    return None


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    import io
    import contextlib
    import os
    import tempfile

    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        assert safe_divide(10, 2) == 5.0, f"safe_divide: {safe_divide(10, 2)}"
        assert safe_divide(1, 0) is None, f"safe_divide: {safe_divide(1, 0)}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r1 = divide_with_else(10, 2)
            r2 = divide_with_else(1, 0)
        assert r1 == 5.0, f"divide_with_else: {r1}"
        assert r2 is None, f"divide_with_else: {r2}"
        assert "计算成功" in buf.getvalue(), f"else 没执行: {buf.getvalue()!r}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert read_int("42") == 42, f"read_int: {read_int('42')}"
        assert read_int("abc") is None, f"read_int: {read_int('abc')}"
        assert read_int(None) is None, f"read_int: {read_int(None)}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert validate_age(25) == "年龄有效", f"validate_age: {validate_age(25)}"
        got_error = False
        try:
            validate_age(-1)
        except ValueError:
            got_error = True
        assert got_error, "validate_age(-1) 应抛 ValueError"
        got_error = False
        try:
            validate_age(200)
        except ValueError:
            got_error = True
        assert got_error, "validate_age(200) 应抛 ValueError"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert check_score(85) == "合格", f"check_score: {check_score(85)}"
        got_error = False
        try:
            check_score(150)
        except ValueError:
            got_error = True
        assert got_error, "check_score(150) 应抛 ValueError"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert check_positive(5) == "是正数", f"check_positive: {check_positive(5)}"
        got_error = False
        try:
            check_positive(-1)
        except AssertionError:
            got_error = True
        assert got_error, "check_positive(-1) 应抛 AssertionError"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert process(True) == "OK", f"process: {process(True)}"
        got_error = False
        try:
            process(False)
        except MyError:
            got_error = True
        assert got_error, "process(False) 应抛 MyError"
        assert issubclass(MyError, Exception), "MyError 必须继承 Exception"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        got_error = False
        try:
            outer()
        except RuntimeError as e:
            got_error = True
            assert isinstance(e.__cause__, ValueError), f"异常链原因: {e.__cause__}"
        assert got_error, "outer() 应抛 RuntimeError"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        tmp = os.path.join(tempfile.gettempdir(), "day21_test.txt")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("hello day21")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r1 = safe_open(tmp)
            r2 = safe_open(tmp + "_不存在")
        assert r1 == "hello day21", f"safe_open: {r1!r}"
        assert r2 is None, f"safe_open: {r2!r}"
        assert buf.getvalue().count("已结束") >= 2, f"finally 没执行: {buf.getvalue()!r}"
        os.remove(tmp)
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert parse("42") == 42, f"parse: {parse('42')}"
        got_error = False
        try:
            parse("abc")
        except NumberError:
            got_error = True
        except ValueError:
            raise AssertionError("应抛 NumberError 而不是 ValueError")
        assert got_error, "parse('abc') 应抛 NumberError"
        assert issubclass(NumberError, Exception), "NumberError 必须继承 Exception"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  异常进阶掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
