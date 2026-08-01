"""
Day 6 · 四大容器综合串讲 练习 (2026.8.1)
=============================================
今天把 List / Tuple / Dict / Set 放在一起对比练习。
完成后在终端运行 python Day6_四大容器串讲练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 选对容器（10 分）
# 题目：根据场景选择最合适的容器类型，创建对应的容器
#   1. 一周七天（固定不变）→ 用什么容器？
#   2. 购物车（要增删改）→ 用什么容器？
#   3. 学号→姓名的映射（按学号查）→ 用什么容器？
#   4. 用户 ID 列表（要去重）→ 用什么容器？
# ============================================================
def problem1():
    week = ("周一","周二","周三","周四","周五","周六","周日")          # 请修改：一周七天（用中文，如"周一"~"周日"）
    cart = ["牛奶","面包"]          # 请修改：购物车，初始有 "牛奶", "面包"
    student_map = {"001": "张三", "002": "李四"}   # 请修改：{"001": "张三", "002": "李四"}
    user_ids = set([101, 102, 101, 103, 102])      # 请修改：从 [101, 102, 101, 103, 102] 去重
    return week, cart, student_map, user_ids


# ============================================================
# 练习 2 · 容器转换（10 分）
# 题目：完成以下容器转换
#   1. 把元组 (1, 2, 3) 转成列表
#   2. 把列表 [1, 2, 2, 3] 转成集合（自动去重）
#   3. 把字典 {"a": 1, "b": 2} 的 key 转成列表
#   4. 把 [("x", 1), ("y", 2)] 转成字典
# ============================================================
def problem2():
    t = (1, 2, 3)
    lst = [1, 2, 2, 3]
    d = {"a": 1, "b": 2}
    pairs = [("x", 1), ("y", 2)]
    
    result1 = list(t)  # 请修改：元组转列表
    result2 = set(lst)     # 请修改：列表转集合
    result3 = list(d.keys())  # 请修改：字典 key 转列表
    result4 = dict(pairs)  # 请修改：列表转字典
    
    return result1, result2, result3, result4


# ============================================================
# 练习 3 · 词频统计 + 去重（10 分）
# 题目：给定一段文本，分别：
#   1. 统计每个单词出现次数（字典）
#   2. 提取不重复的单词（集合）
#   3. 所有单词按顺序保存（列表）
# ============================================================
def problem3():
    text = "apple banana apple orange banana apple"
    
    freq = {"apple": text.count("apple"), "banana": text.count("banana"), "orange": text.count("orange")}       # 请修改：{"apple": 3, "banana": 2, "orange": 1}
    unique = set(text.split())     # 请修改：{"apple", "banana", "orange"}
    words = text.split()     # 请修改：["apple", "banana", "apple", "orange", "banana", "apple"]
    
    return freq, unique, words


# ============================================================
# 练习 4 · 集合运算（10 分）
# 题目：两个班的学生，用集合运算完成：
#   1. 两个班都有的学生
#   2. 只在 A 班的学生
#   3. 所有学生（去重）
# ============================================================
def problem4():
    class_a = {"张三", "李四", "王五"}
    class_b = {"王五", "赵六", "孙七"}
    
    common = class_a & class_b    # 请修改：两个班都有的
    only_a = class_a - (class_a & class_b)    # 请修改：只在 A 班的
    all_stu = class_a |class_b   # 请修改：所有学生
    
    return common, only_a, all_stu


# ============================================================
# 练习 5 · 学生成绩处理（10 分）
# 题目：学生成绩嵌套字典（学号 → 姓名+各科成绩）
#   1. 计算每个学生的总分
#   2. 找出总分最高的学号
#   3. 返回总成绩排名（学号列表，从高到低）
# ============================================================
def problem5():
    students = {
        "001": {"name": "张三", "scores": [95, 87, 92]},
        "002": {"name": "李四", "scores": [78, 90, 85]},
        "003": {"name": "王五", "scores": [88, 76, 95]},
    }
    
    totals = {"001":sum(students["001"]["scores"]),
              "002":sum(students["002"]["scores"]),
              "003":sum(students["003"]["scores"])
    }    # 请修改：学号 → 总分
    top_student = max(students,key = totals.get)  # 请修改：总分最高的学号
    ranking = sorted(students, key = totals.get,reverse=True)      # 请修改：按总分从高到低的学号列表
    
    return totals, top_student, ranking


# ============================================================
# 练习 6 · 查找与判断（10 分）
# 题目：给定数据，完成以下判断
#   1. 某个元素是否在列表中
#   2. 某个 key 是否在字典中（用 in）
#   3. 某个元素是否在集合中
#   4. 用 get 安全取值
# ============================================================
def problem6():
    lst = [1, 2, 3, 4, 5]
    d = {"name": "示其", "age": 18}
    s = {10, 20, 30}
    
    in_list = 3 in lst           # 请修改：3 是否在列表中
    key_exists = "age" in d      # 请修改："age" 是否是字典的 key
    in_set = 25 in s             # 请修改：25 是否在集合中
    safe_get = d.get("city","未知")              # 请修改：用 get 取 "city"，默认值 "未知"
    
    return in_list, key_exists, in_set, safe_get


# ============================================================
# 练习 7 · 成绩评级（10 分）
# 题目：给定学生成绩字典，把每个学生分到等级组
# >= 90：优秀    >= 80：良好    >= 60：及格    其他：不及格
# 返回 等级 → [学生名] 的字典
# ============================================================
def problem7():
    scores = {"张三": 95, "李四": 82, "王五": 65, "赵六": 45, "陈七": 90}
    
    groups = {
        "优秀": [name for name,score in scores.items() if score >= 90],
        "良好": [name for name,score in scores.items() if score >= 80 and score < 90],
        "及格": [name for name,score in scores.items() if score >= 60 and score < 80],
        "不及格": [name for name,score in scores.items() if score <= 60 ]
    }
    # 请在此处编写代码
    
    return groups


# ============================================================
# 练习 8 · 实战：通讯录管理系统（10 分）
# 题目：用嵌套字典实现一个通讯录
# 结构：{"姓名": {"phone": "电话", "city": "城市", "tags": ["标签1", "标签2"]}}
# 实现以下两个函数：
#   1. add_contact(contacts, name, phone, city): 添加联系人，返回新字典
#   2. search(contacts, name): 查找联系人，返回 (phone, city)，不存在返回 None
# ============================================================
dct1 = {}
def add_contact(contacts, name, phone, city):
    """添加联系人，返回新字典"""
    # 请在此处编写代码
    contacts[name] = {"phone": phone,"city" : city,}
    return contacts

def search(contacts, name):
    """查找联系人，返回 (phone, city)，不存在返回 None"""
    # 请在此处编写代码
    info = contacts.get(name)
    if info:
        return(info["phone"],info["city"])
    return None
    


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        week, cart, sm, uids = problem1()
        assert week == ("周一", "周二", "周三", "周四", "周五", "周六", "周日"), f"week 错误: {week}"
        assert cart == ["牛奶", "面包"], f"cart 错误: {cart}"
        assert sm == {"001": "张三", "002": "李四"}, f"student_map 错误: {sm}"
        assert uids == {101, 102, 103}, f"user_ids 错误: {uids}"
        score += 10
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r1, r2, r3, r4 = problem2()
        assert r1 == [1, 2, 3], f"元组转列表: {r1}"
        assert r2 == {1, 2, 3}, f"列表转集合: {r2}"
        assert r3 == ["a", "b"], f"key转列表: {r3}"
        assert r4 == {"x": 1, "y": 2}, f"列表转字典: {r4}"
        score += 10
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        freq, unique, words = problem3()
        assert freq == {"apple": 3, "banana": 2, "orange": 1}, f"词频: {freq}"
        assert unique == {"apple", "banana", "orange"}, f"去重: {unique}"
        assert words == ["apple", "banana", "apple", "orange", "banana", "apple"], f"列表: {words}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    try:
        common, only_a, all_stu = problem4()
        assert common == {"王五"}, f"共有: {common}"
        assert only_a == {"张三", "李四"}, f"只在A: {only_a}"
        assert all_stu == {"张三", "李四", "王五", "赵六", "孙七"}, f"所有: {all_stu}"
        score += 10
        print("[PASS] 第 4 题")
    except Exception as e:
        print(f"[FAIL] 第 4 题: {e}")

    # 第 5 题
    try:
        totals, top, ranking = problem5()
        assert totals == {"001": 274, "002": 253, "003": 259}, f"总分: {totals}"
        assert top == "001", f"最高: {top}"
        assert ranking == ["001", "003", "002"], f"排名: {ranking}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        a, b, c, d = problem6()
        assert a == True, f"3在列表中: {a}"
        assert b == True, f"age是key: {b}"
        assert c == False, f"25在集合中应为False: {c}"
        assert d == "未知", f"get默认值: {d}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        groups = problem7()
        assert groups["优秀"] == ["张三", "陈七"], f"优秀: {groups['优秀']}"
        assert groups["良好"] == ["李四"], f"良好: {groups['良好']}"
        assert groups["及格"] == ["王五"], f"及格: {groups['及格']}"
        assert groups["不及格"] == ["赵六"], f"不及格: {groups['不及格']}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        contacts = {}
        contacts = add_contact(contacts, "张三", "13800138000", "重庆")
        contacts = add_contact(contacts, "李四", "13900139000", "北京")
        assert contacts["张三"] == {"phone": "13800138000", "city": "重庆"}, f"添加错误: {contacts}"
        r = search(contacts, "张三")
        assert r == ("13800138000", "重庆"), f"查找错误: {r}"
        r = search(contacts, "王五")
        assert r is None, f"不存在应返回None: {r}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 80")
    print(f"{'='*40}")
    if score >= 70:
        print("  四大容器已融会贯通！")
    elif score >= 50:
        print("  大部分掌握，个别知识点需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
