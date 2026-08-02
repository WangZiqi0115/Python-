"""
Day 8 · 函数专题 练习 (2026.8.2)
==================================
今天的题目专门针对你前七天犯过的错误设计。
完成后在终端运行 python Day8_函数专题练习.py 会自动评分。
"""

# ============================================================
# 练习 1 · 函数定义与调用（5 分）
# 题目：定义一个函数 add(a, b)，返回两数之和
# ============================================================
def add(a, b):
    # 请在此处编写代码
    return a + b


# ============================================================
# 练习 2 · 忘加括号的坑（5 分）
# 题目：下面的函数想返回 "HELLO"，但有一个 bug，请修复
# ============================================================
def shout(text):
    return text.upper()   # ❌ 这里有个 bug，请修复


# ============================================================
# 练习 3 · 返回值 vs None（10 分）
# 题目：完成以下函数
#   1. add_item(lst, item)：向列表添加元素，返回修改后的列表
#      （不要犯 new_list = lst.append(item) 的错误）
#   2. count_occurrences(text, char)：统计字符出现次数，返回数字
# ============================================================
def add_item(lst, item):
    # 请在此处编写代码
    lst.append(item)
    return lst

def count_occurrences(text, char):
    # 请在此处编写代码
    count = 0
    for word in text:
        if word == char:
            count += 1
    return count


# ============================================================
# 练习 4 · 参数与作用域（10 分）
# 题目：阅读代码，写出最终输出（填在注释里）
# 然后在终端运行验证
#
# x = 10
# def change():
#     x = 20
#     return x
# print(change())     # 输出：20
# print(x)            # 输出: 10
# ============================================================
def problem4():
    # change() 输出：20
    # x 输出：10
    pass


# ============================================================
# 练习 5 · 默认参数陷阱（10 分）
# 题目：修复下面的函数，使每次不传列表时都得到独立的列表
# ============================================================
def add_task(task, task_list=[]):   # ❌ 默认列表会共享
    task_list.append(task)
    return task_list

def add_task_fixed(task, task_list=None):
    if task_list == None:
        task_list = []
    task_list.append(task)
    return task_list


# ============================================================
# 练习 6 · 函数作为参数（10 分）
# 题目：用 sorted 的 key 参数完成排序
#   1. 按分数从高到低排序学生
#   2. 按字符串长度排序单词
# ============================================================
def problem6():
    students = [("张三", 95), ("李四", 82), ("王五", 90)]
    words = ["python", "java", "c", "kotlin"]
    
    by_score = sorted(students,key = lambda x: x[1],reverse=True)   # 请修改：按分数从高到低，用 lambda
    by_length = sorted(words,key=len)  # 请修改：按长度排序，用 len
    
    return by_score, by_length


# ============================================================
# 练习 7 · 综合：成绩统计函数（10 分）
# 题目：实现函数 analyze_scores(scores)
# 返回（最高分, 最低分, 平均分保留1位, 及格率保留1位）
# 及格：>= 60
# ============================================================
def analyze_scores(scores):
    """
    示例：
    analyze_scores([70, 55, 90, 45, 88]) -> (90, 45, 69.6, 60.0)
    """
    # 请在此处编写代码
    max_score = max(scores)
    min_score = min(scores)
    jun_score = round(sum(scores) / len(scores),1)
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    percent = round(count / len(scores),1)
    return (max_score, min_score, jun_score, percent)


# ============================================================
# 练习 8 · 实战：学生管理函数集（10 分）
# 题目：实现三个函数
#   1. add_student(students, sid, name, score)：添加学生
#      结构：{"001": {"name": "张三", "score": 95}}
#      返回修改后的字典
#   2. get_student(students, sid)：查询学生，返回 (name, score)，不存在返回 None
#   3. top_students(students, n)：返回成绩最高的 n 个学生的名字列表
# ============================================================
def add_student(students, sid, name, score):
    """添加学生，返回修改后的字典"""
    # 请在此处编写代码
    students[sid] = {"name":name,"score":score}
    return students

def get_student(students, sid):
    """查询学生，返回 (name, score)，不存在返回 None"""
    # 请在此处编写代码
    info = students.get(sid)
    if info:
        return(info["name"],info["score"])
    return None
    

def top_students(students, n):
    """返回成绩最高的 n 个学生的名字列表"""
    # 请在此处编写代码
    rank = sorted(students.items(),key = lambda x:x[1]["score"],reverse=True)
    lst =[]
    for sid,info in rank[:n]:
        lst.append(info["name"])
    return lst


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    score = 0
    print("=" * 40)

    # 第 1 题
    try:
        assert add(3, 5) == 8, f"add(3,5) 应为 8，得到 {add(3,5)}"
        assert add(-1, 1) == 0, f"add(-1,1) 应为 0，得到 {add(-1,1)}"
        score += 5
        print("[PASS] 第 1 题")
    except Exception as e:
        print(f"[FAIL] 第 1 题: {e}")

    # 第 2 题
    try:
        r = shout("hello")
        assert r == "HELLO", f"应为 HELLO，得到 {r}"
        score += 5
        print("[PASS] 第 2 题")
    except Exception as e:
        print(f"[FAIL] 第 2 题: {e}")

    # 第 3 题
    try:
        lst = [1, 2]
        r1 = add_item(lst, 3)
        assert r1 == [1, 2, 3], f"add_item 应为 [1,2,3]，得到 {r1}"
        r2 = count_occurrences("banana", "a")
        assert r2 == 3, f"count_occurrences 应为 3，得到 {r2}"
        score += 10
        print("[PASS] 第 3 题")
    except Exception as e:
        print(f"[FAIL] 第 3 题: {e}")

    # 第 4 题
    score += 10
    print("[PASS] 第 4 题（请在注释中填写预测）")

    # 第 5 题
    try:
        r1 = add_task_fixed("学习")
        r2 = add_task_fixed("运动")
        assert r1 == ["学习"], f"第一次调用应为 ['学习']，得到 {r1}"
        assert r2 == ["运动"], f"第二次调用应为 ['运动']，得到 {r2}"
        score += 10
        print("[PASS] 第 5 题")
    except Exception as e:
        print(f"[FAIL] 第 5 题: {e}")

    # 第 6 题
    try:
        by_score, by_length = problem6()
        assert by_score == [("张三", 95), ("王五", 90), ("李四", 82)], f"按分数排序: {by_score}"
        assert by_length == ["c", "java", "python", "kotlin"], f"按长度排序: {by_length}"
        score += 10
        print("[PASS] 第 6 题")
    except Exception as e:
        print(f"[FAIL] 第 6 题: {e}")

    # 第 7 题
    try:
        r = analyze_scores([70, 55, 90, 45, 88])
        assert r[0] == 90, f"最高分应为 90，得到 {r[0]}"
        assert r[1] == 45, f"最低分应为 45，得到 {r[1]}"
        assert abs(r[2] - 69.6) < 0.1, f"平均分约为 69.6，得到 {r[2]}"
        assert abs(r[3] - 60.0) < 0.1, f"及格率应为 60.0，得到 {r[3]}"
        score += 10
        print("[PASS] 第 7 题")
    except Exception as e:
        print(f"[FAIL] 第 7 题: {e}")

    # 第 8 题
    try:
        students = {}
        students = add_student(students, "001", "张三", 95)
        students = add_student(students, "002", "李四", 82)
        students = add_student(students, "003", "王五", 90)
        assert students["001"] == {"name": "张三", "score": 95}, f"添加错误: {students}"
        r = get_student(students, "001")
        assert r == ("张三", 95), f"查询错误: {r}"
        r = get_student(students, "999")
        assert r is None, f"不存在应返回 None: {r}"
        top = top_students(students, 2)
        assert top == ["张三", "王五"], f"前两名: {top}"
        score += 10
        print("[PASS] 第 8 题")
    except Exception as e:
        print(f"[FAIL] 第 8 题: {e}")

    # 总分
    print(f"\n{'='*40}")
    print(f"  总分: {score} / 70")
    print(f"{'='*40}")
    if score >= 60:
        print("  函数专题掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
