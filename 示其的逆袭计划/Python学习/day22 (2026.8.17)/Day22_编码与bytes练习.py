"""
Day 22 · 编码与 bytes 练习 (2026.8.17)
====================================
完成后在终端运行 python Day22_编码与bytes练习.py 会自动评分。
先看懂 Day22_编码与bytes知识点.py 的例题，再做下面的题。
"""


# ============================================================
# 练习 1 · 打包：str → bytes（10 分）
# to_utf8(s)：把字符串按 utf-8 编码成 bytes
# 例：to_utf8("abc") -> b"abc"，to_utf8("你好") -> "你好".encode()
# 提示：str.encode（默认 utf-8）
# ============================================================
def to_utf8(s):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 2 · 拆包：bytes → str（10 分）
# from_utf8(b)：把 utf-8 编码的 bytes 解码成字符串
# 例：from_utf8("你好".encode()) -> "你好"
# 提示：bytes.decode（默认 utf-8）
# ============================================================
def from_utf8(b):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 3 · 字符个数（10 分）
# count_chars(s)：返回字符串的字符个数
# 例：count_chars("你好abc") -> 5
# 提示：len（对 str 数字符）
# ============================================================
def count_chars(s):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 4 · 字节个数（10 分）
# count_bytes_utf8(s)：返回字符串按 utf-8 编码后的字节个数
# 例：count_bytes_utf8("你好abc") -> 9（中文 2×3 + 英文 3×1）
# 提示：先 .encode("utf-8") 再 len
# ============================================================
def count_bytes_utf8(s):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 5 · GBK 打包（10 分）
# to_gbk(s)：把字符串按 gbk 编码成 bytes
# 例：to_gbk("你好") == "你好".encode("gbk")
# 提示：str.encode
# ============================================================
def to_gbk(s):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 6 · 用对编码修复乱码（10 分）
# decode_gbk(b)：把 gbk 编码的 bytes 解码成字符串
# 例：msg = "今天".encode("gbk")；decode_gbk(msg) -> "今天"
# 提示：bytes.decode
# ============================================================
def decode_gbk(b):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 7 · bytes 索引（10 分）
# first_byte(b)：返回 bytes 的第一个字节值（整数）
# 例：first_byte(b"abc") -> 97（即 ord("a")）
# 提示：b[0]
# ============================================================
def first_byte(b):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 8 · ord 和 chr（10 分）
# code_of(ch)：返回字符的编号 ord(ch)
# char_of(code)：返回编号对应的字符 chr(code)
# 例：code_of("A") -> 65；char_of(97) -> "a"
# 提示：ord / chr
# ============================================================
def code_of(ch):
    # 请在此处编写代码
    return None


def char_of(code):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 9 · 判断是否全是 ASCII（10 分）
# is_ascii(s)：字符串里所有字符编号都 < 128 返回 True，否则 False
# 例：is_ascii("abc123") -> True；is_ascii("你好") -> False
# 提示：ord(c) < 128，配合 all()
# ============================================================
def is_ascii(s):
    # 请在此处编写代码
    return None


# ============================================================
# 练习 10 · 综合：字节的十六进制（10 分）
# utf8_hex(s)：把字符串按 utf-8 编码后，转成十六进制字符串
# 例：utf8_hex("A") -> "41"；utf8_hex("你") -> "e4bda0"
# 提示：.encode("utf-8") 后 .hex()
# ============================================================
def utf8_hex(s):
    # 请在此处编写代码
    return None


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        assert to_utf8("abc") == b"abc", f"to_utf8: {to_utf8('abc')!r}"
        assert to_utf8("你好") == "你好".encode(), f"to_utf8: {to_utf8('你好')!r}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        assert from_utf8("你好".encode()) == "你好", f"from_utf8: {from_utf8('你好'.encode())!r}"
        assert from_utf8(b"abc") == "abc", f"from_utf8: {from_utf8(b'abc')!r}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        assert count_chars("你好abc") == 5, f"count_chars: {count_chars('你好abc')}"
        assert count_chars("") == 0, f"count_chars: {count_chars('')}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert count_bytes_utf8("你好abc") == 9, f"count_bytes_utf8: {count_bytes_utf8('你好abc')}"
        assert count_bytes_utf8("A") == 1, f"count_bytes_utf8: {count_bytes_utf8('A')}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        assert to_gbk("你好") == "你好".encode("gbk"), f"to_gbk: {to_gbk('你好')!r}"
        assert to_gbk("A") == b"A", f"to_gbk: {to_gbk('A')!r}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        msg = "今天".encode("gbk")
        assert decode_gbk(msg) == "今天", f"decode_gbk: {decode_gbk(msg)!r}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert first_byte(b"abc") == 97, f"first_byte: {first_byte(b'abc')}"
        assert first_byte(b"z") == 122, f"first_byte: {first_byte(b'z')}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert code_of("A") == 65, f"code_of: {code_of('A')}"
        assert code_of("你") == ord("你"), f"code_of: {code_of('你')}"
        assert char_of(97) == "a", f"char_of: {char_of(97)!r}"
        assert char_of(20320) == "你", f"char_of: {char_of(20320)!r}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        assert is_ascii("abc123") is True, f"is_ascii: {is_ascii('abc123')}"
        assert is_ascii("你好") is False, f"is_ascii: {is_ascii('你好')}"
        assert is_ascii("a你b") is False, f"is_ascii: {is_ascii('a你b')}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        assert utf8_hex("A") == "41", f"utf8_hex: {utf8_hex('A')!r}"
        assert utf8_hex("你") == "e4bda0", f"utf8_hex: {utf8_hex('你')!r}"
        assert utf8_hex("OK") == "4f4b", f"utf8_hex: {utf8_hex('OK')!r}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  编码与 bytes 掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
