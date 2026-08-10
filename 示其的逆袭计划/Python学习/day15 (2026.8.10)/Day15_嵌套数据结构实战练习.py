"""
Day 15 · 嵌套数据结构实战 练习 (2026.8.10)
====================================
完成后在终端运行 python Day15_嵌套数据结构实战练习.py 会自动评分。
"""


# 测试会用到这组数据，可以先看明白它的形状：
students = [
    {"name": "张三", "score": 88, "city": "重庆"},
    {"name": "李四", "score": 95, "city": "北京"},
    {"name": "王五", "score": 72, "city": "重庆"},
    {"name": "赵六", "score": 90, "city": "上海"},
]


# ============================================================
# 练习 1 · 取第一个学生姓名（10 分）
# 从 students 中返回第一个学生的 name
# 例：get_first_name(students) -> "张三"
# ============================================================
def get_first_name(students):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 2 · 取嵌套成绩（10 分）
# 从 scores 中取指定学生的指定科目成绩
# scores = {"张三": {"语文": 90, "数学": 85}, "李四": {"语文": 78, "数学": 92}}
# 例：get_score(scores, "李四", "数学") -> 92
# ============================================================
def get_score(scores, name, subject):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 3 · 计算平均分（10 分）
# student = {"name": "张三", "scores": [95, 87, 92]}
# 返回分数的平均分，保留 1 位小数
# 例：avg_score(student) -> 91.3
# ============================================================
def avg_score(student):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 4 · 按分数排序（10 分）
# 按 score 从高到低排序，返回学生姓名列表
# 例：sort_by_score(students) -> ["李四", "赵六", "张三", "王五"]
# ============================================================
def sort_by_score(students):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 5 · 按城市分组（10 分）
# people = [{"name": "张三", "city": "重庆"}, ...]
# 返回 {"重庆": ["张三", "王五"], "北京": ["李四"]}
# 提示：用 defaultdict(list)
# ============================================================
def group_by_city(people):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 6 · 反转字典（10 分）
# 把 {"张三": 95, "李四": 82} 转成 {95: "张三", 82: "李四"}
# 要求用字典推导式
# ============================================================
def reverse_dict(d):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 7 · 合并字典（10 分）
# 合并 d1 和 d2，d2 的键值覆盖 d1
# 例：merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
#     -> {"a": 1, "b": 3, "c": 4}
# ============================================================
def merge_dicts(d1, d2):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 8 · 提取所有姓名（10 分）
# 返回 students 中所有人的 name 组成的列表
# 例：get_names(students) -> ["张三", "李四", "王五", "赵六"]
# 提示：列表推导式
# ============================================================
def get_names(students):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 9 · 二维列表扁平化（10 分）
# 把 [[1, 2, 3], [4, 5, 6]] 变成 [1, 2, 3, 4, 5, 6]
# 提示：嵌套列表推导式，外层 for 在前
# ============================================================
def flatten(matrix):
    # 请在此处编写代码
    pass


# ============================================================
# 练习 10 · 多层安全取值（10 分）
# data = {"a": {"b": {"c": 42}}}
# safe_get(data, "a", "b", "c") -> 42
# safe_get(data, "a", "x") -> None
# 取不到时返回 None，不能报错
# ============================================================
def safe_get(data, *keys):
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
        assert get_first_name(students) == "张三", f"get_first_name: {get_first_name(students)}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        scores = {"张三": {"语文": 90, "数学": 85}, "李四": {"语文": 78, "数学": 92}}
        assert get_score(scores, "李四", "数学") == 92, f"get_score: {get_score(scores, '李四', '数学')}"
        assert get_score(scores, "张三", "语文") == 90, f"get_score: {get_score(scores, '张三', '语文')}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        student = {"name": "张三", "scores": [95, 87, 92]}
        assert avg_score(student) == 91.3, f"avg_score: {avg_score(student)}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        assert sort_by_score(students) == ["李四", "赵六", "张三", "王五"], f"sort_by_score: {sort_by_score(students)}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        people = [
            {"name": "张三", "city": "重庆"},
            {"name": "李四", "city": "北京"},
            {"name": "王五", "city": "重庆"},
        ]
        assert group_by_city(people) == {"重庆": ["张三", "王五"], "北京": ["李四"]}, f"group_by_city: {group_by_city(people)}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        assert reverse_dict({"张三": 95, "李四": 82}) == {95: "张三", 82: "李四"}, f"reverse_dict: {reverse_dict({'张三': 95, '李四': 82})}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}, f"merge_dicts: {merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        assert get_names(students) == ["张三", "李四", "王五", "赵六"], f"get_names: {get_names(students)}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 第 9 题
    try:
        assert flatten([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6], f"flatten: {flatten([[1, 2, 3], [4, 5, 6]])}"
        score += 10
        print("[PASS] 第 9 题")
    except Exception as e:
        print(f"[FAIL] 第 9 题: {e}")

    # 第 10 题
    try:
        data = {"a": {"b": {"c": 42}}}
        assert safe_get(data, "a", "b", "c") == 42, f"safe_get: {safe_get(data, 'a', 'b', 'c')}"
        assert safe_get(data, "a", "x") is None, f"safe_get 缺失键: {safe_get(data, 'a', 'x')}"
        assert safe_get([1, 2, 3], 5) is None, f"safe_get 越界: {safe_get([1, 2, 3], 5)}"
        score += 10
        print("[PASS] 第 10 题")
    except Exception as e:
        print(f"[FAIL] 第 10 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 100")
    print(f"{'='*40}")
    if score >= 80:
        print("  嵌套数据结构掌握得很扎实！")
    elif score >= 50:
        print("  基本概念清楚了，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
