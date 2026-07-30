"""
Day 4 · Set 集合 练习 (2026.7.30)
===================================
今天学了集合的创建、增删、集合运算、推导式。
完成后在终端运行 python Day4_Set练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 创建集合（5 分）
# 题目：按要求创建以下集合
#   1. 创建集合 s1，包含 1, 2, 3, 4, 5
#   2. 创建空集合 s2
#   3. 从列表 [1, 2, 2, 3, 3, 4] 创建集合 s3（自动去重）
#   4. 从字符串 "banana" 创建集合 s4
# ============================================================
def problem1():
    s1 = None  # 请修改
    s2 = None  # 请修改
    s3 = None  # 请修改
    s4 = None  # 请修改
    return s1, s2, s3, s4


# ============================================================
# 练习 2 · 集合增删（5 分）
# 题目：对集合 s = {1, 2, 3} 依次操作
#   1. 添加 4
#   2. 用 remove 删除 2
#   3. 用 discard 删除 99（不存在的元素）
#   4. 添加 5
#   5. 最后返回 s
# ============================================================
def problem2():
    s = {1, 2, 3}
    # 请在此处编写代码
    
    return s  # 应返回 {1, 3, 4, 5}


# ============================================================
# 练习 3 · 集合运算（10 分）
# 题目：给定两个集合 a 和 b，分别求并集、交集、差集(a-b)、对称差集
# ============================================================
def problem3():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    
    union = None       # 请修改：并集
    intersection = None  # 请修改：交集
    difference = None  # 请修改：差集 (a - b)
    sym_diff = None    # 请修改：对称差集
    
    return union, intersection, difference, sym_diff


# ============================================================
# 练习 4 · 判断子集（10 分）
# 题目：给定三个集合，判断 c 是否是 a 的子集，
# a 和 b 是否有交集，d 和 a 是否不相交
# ============================================================
def problem4():
    a = {1, 2, 3, 4, 5}
    c = {2, 3}
    d = {6, 7}
    
    is_subset = None      # 请修改：c 是否是 a 的子集
    has_intersection = None  # 请修改：a 和 b 是否有交集（提示：& 或 isdisjoint）
    is_disjoint = None     # 请修改：a 和 d 是否不相交
    
    return is_subset, has_intersection, is_disjoint


# ============================================================
# 练习 5 · 集合去重（10 分）
# 题目：给定一个列表，分别用 set 和 dict.fromkeys 去重
# 观察两者的区别（顺序是否保留）
# ============================================================
def problem5():
    items = [3, 1, 2, 1, 3, 4, 2, 5, 1]
    
    result_set = None      # 请修改：用 set 去重
    result_ordered = None  # 请修改：用 dict.fromkeys 去重并保留顺序
    
    return result_set, result_ordered


# ============================================================
# 练习 6 · 集合推导式（10 分）
# 题目：用集合推导式（一行语句）完成
#   1. 生成 1~20 中所有奇数的平方组成的集合
#   2. 找出两个列表中相同的元素组成的集合
# ============================================================
def problem6():
    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    list_b = [5, 6, 7, 8, 9, 10]
    
    squares = None  # 请修改：奇数平方的集合
    common = None   # 请修改：list_a 和 list_b 的公共元素集合
    
    return squares, common


# ============================================================
# 练习 7 · 两列表差异分析（10 分）
# 题目：有两个班级的学生名单（可能有重复），用集合运算找出：
#   1. 两个班都有的学生
#   2. 只在 A 班的学生
#   3. 只在 B 班的学生
#   4. 所有不重复的学生
# ============================================================
def problem7():
    class_a = {"张三", "李四", "王五", "赵六"}
    class_b = {"王五", "赵六", "陈七", "周八"}
    
    both = None     # 请修改：两个班都有的
    only_a = None   # 请修改：只在 A 班的
    only_b = None   # 请修改：只在 B 班的
    all_students = None  # 请修改：所有不重复的学生
    
    return both, only_a, only_b, all_students


# ============================================================
# 练习 8 · 实战：投票统计（10 分）
# 题目：一次投票中，每个人可以投多票（名单有重复），
# 完成以下统计：
#   1. 总共有多少位不同的候选人（去重）
#   2. 统计每位候选人获得的票数（用字典）
#   3. 找出得票最多的候选人
# ============================================================
def problem8():
    votes = ["张三", "李四", "张三", "王五", "李四", "张三", "赵六", "李四", "张三"]
    
    unique_count = None  # 请修改：不同的候选人数
    vote_count = {}      # 请修改：统计每个人得了多少票
    
    winner = None        # 请修改：得票最多的人
    
    return unique_count, vote_count, winner


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        s1, s2, s3, s4 = problem1()
        assert s1 == {1, 2, 3, 4, 5}, f"s1 错误: {s1}"
        assert s2 == set(), f"s2 应为空集合: {s2}"
        assert s3 == {1, 2, 3, 4}, f"s3 应为 {{1,2,3,4}}: {s3}"
        assert s4 == {"b", "a", "n"}, f"s4 应为 {{\"b\",\"a\",\"n\"}}: {s4}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        result = problem2()
        assert result == {1, 3, 4, 5}, f"预期 {{1,3,4,5}}，得到 {result}"
        score += 5
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        u, i, d, sd = problem3()
        assert u == {1, 2, 3, 4, 5, 6, 7, 8}, f"并集错误: {u}"
        assert i == {4, 5}, f"交集错误: {i}"
        assert d == {1, 2, 3}, f"差集错误: {d}"
        assert sd == {1, 2, 3, 6, 7, 8}, f"对称差集错误: {sd}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        sub, has_inter, dis = problem4()
        assert sub == True, f"c 是 a 的子集应为 True，得到 {sub}"
        assert has_inter == True, f"a 和 b 应有交集：{has_inter}"
        assert dis == True, f"a 和 d 应不相交：{dis}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        r1, r2 = problem5()
        assert set(r1) == {1, 2, 3, 4, 5}, f"set去重结果应为 {1,2,3,4,5}：{r1}"
        assert r2 == [3, 1, 2, 4, 5], f"dict去重应保持顺序 [3,1,2,4,5]：{r2}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        squares, common = problem6()
        assert squares == {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}, f"奇数平方错误: {squares}"
        assert common == {5, 6, 7, 8}, f"公共元素错误: {common}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        both, only_a, only_b, all_s = problem7()
        assert both == {"王五", "赵六"}, f"两班共有: {both}"
        assert only_a == {"张三", "李四"}, f"只在A班: {only_a}"
        assert only_b == {"陈七", "周八"}, f"只在B班: {only_b}"
        assert all_s == {"张三", "李四", "王五", "赵六", "陈七", "周八"}, f"所有学生: {all_s}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        count, vc, winner = problem8()
        assert count == 4, f"不同候选人应为 4：{count}"
        assert vc == {"张三": 4, "李四": 3, "王五": 1, "赵六": 1}, f"票数统计错误: {vc}"
        assert winner == "张三", f"得票最多应为 张三：{winner}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 70")
    print(f"{'='*40}")
    if score >= 60:
        print("  集合掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
