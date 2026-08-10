# Day 15 · 嵌套数据结构实战 知识点速查 (2026.8.10)
# ============================================
# 今天专门练"list 套 dict、dict 套 list、dict 套 dict"这类真实数据。
# 爬虫、数模、刷题里见到的数据，几乎都是这种形状。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。


# ============================================================
# 一、为什么要有嵌套结构
# ============================================================
# 一个学生有多个属性，就用 dict 存：
student = {"name": "张三", "score": 95, "city": "重庆"}

# 一个班级有很多学生，就把多个 dict 装进 list：
students = [
    {"name": "张三", "score": 95, "city": "重庆"},
    {"name": "李四", "score": 82, "city": "北京"},
    {"name": "王五", "score": 90, "city": "重庆"},
]

# 一个学生有多科成绩，可以在 dict 里再放一个 dict：
scores = {
    "张三": {"语文": 90, "数学": 85},
    "李四": {"语文": 78, "数学": 92},
}

# 一个学生有多科成绩，也可以放 list：
score_list = {
    "张三": [95, 87, 92],
    "李四": [70, 88, 96],
}


# ============================================================
# 二、常见的四种嵌套形状
# ============================================================
# 1. list 套 dict：一批"对象"
#    [{"name": "张三"}, {"name": "李四"}]
#    适合：学生列表、商品列表、爬虫抓回来的每条记录

# 2. dict 套 list：一个"名字"对应一组值
#    {"张三": [95, 87, 92]}
#    适合：每人有多科成绩、每个词出现的位置

# 3. dict 套 dict：一个"名字"对应一组属性
#    {"张三": {"语文": 90, "数学": 85}}
#    适合：按名字查详细资料

# 4. list 套 list：二维表格 / 矩阵
#    [[1, 2, 3], [4, 5, 6]]
#    适合：矩阵、Excel 行数据、地图


# ============================================================
# 三、多层访问：一层一层剥开
# ============================================================
# list 用索引取，dict 用键取，一层一层往里走：

# students[0]           → 第一个学生的整个 dict
# students[0]["name"]   → 第一个学生的名字
# scores["张三"]        → 张三的整个成绩 dict
# scores["张三"]["数学"] → 张三的数学成绩
# score_list["李四"][1] → 李四的第 2 科成绩（索引从 0 数）

# 记忆口诀：先看这一层是 list 还是 dict
#   list → 用 [下标]
#   dict → 用 ["键"]


# ============================================================
# 四、安全取值（重点）
# ============================================================
# 直接取值，键不存在会报 KeyError，索引越界会报 IndexError
data = {"a": {"b": {"c": 42}}}
# data["a"]["x"]   ❌ KeyError

# 方法 1：每一层都用 get
print(data.get("a", {}).get("x", None))     # None

# 方法 2：先判断再取
if "a" in data and "x" in data["a"]:
    print(data["a"]["x"])
else:
    print(None)

# 方法 3：try / except 接住
try:
    value = data["a"]["x"]
except KeyError:
    value = None
print(value)                               # None

# 通用小函数：逐层安全取，取不到返回 None
def safe_get(obj, *keys):
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return None
    return current

print(safe_get(data, "a", "b", "c"))       # 42
print(safe_get(data, "a", "x"))            # None


# ============================================================
# 五、遍历嵌套结构
# ============================================================
# list 套 dict：for 拿到每个 dict，再取键
for stu in students:
    print(stu["name"], stu["score"])

# dict 套 list：for key, value in d.items()
for name, score_list_ in score_list.items():
    print(name, score_list_)                 # 张三 [95, 87, 92]

# dict 套 dict：两层遍历
for name, subject_scores in scores.items():
    for subject, score in subject_scores.items():
        print(name, subject, score)


# ============================================================
# 六、按字段排序（重点）
# ============================================================
# 想按 score 排序，用 key 指定"取哪个字段"
sorted_by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for stu in sorted_by_score:
    print(stu["name"], stu["score"])

# 只取排序后的名字：
names_by_score = [s["name"] for s in sorted_by_score]
# ['李四', '王五', '张三']

# 按多个字段：key=lambda s: (s["score"], s["name"])
# 先比分数，分数相同再比名字


# ============================================================
# 七、分组（重点，非常实用）
# ============================================================
# 把学生按城市分组：城市 → 学生姓名列表
from collections import defaultdict

groups = defaultdict(list)
for stu in students:
    groups[stu["city"]].append(stu["name"])

# groups 是 defaultdict，打印出来像普通字典：
# {'重庆': ['张三', '王五'], '北京': ['李四']}

# 转成普通 dict 再查看更干净：
print(dict(groups))


# ============================================================
# 八、反转 / 合并字典
# ============================================================
# 反转：键变值、值变键（要求值唯一，否则后面的覆盖前面的）
d = {"张三": 95, "李四": 82}
reversed_d = {score: name for name, score in d.items()}
# {95: '张三', 82: '李四'}

# 合并：update 会就地修改；| 返回新字典（Python 3.9+）
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
# d1 = {'a': 1, 'b': 3, 'c': 4}，b 被 d2 覆盖

d3 = {"a": 1, "b": 2} | {"b": 3, "c": 4}
# d3 = {'a': 1, 'b': 3, 'c': 4}


# ============================================================
# 九、提取与扁平化
# ============================================================
# 提取所有学生的名字：列表推导式
all_names = [stu["name"] for stu in students]

# 二维列表扁平化：外层 for 在前，内层 for 在后
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# 提取嵌套 dict 里的所有值（一层）
all_subject_scores = [score for subject_scores in scores.values() for score in subject_scores.values()]
# [90, 85, 78, 92]


# ============================================================
# 十、JSON 结构预览（Day 24 会系统学）
# ============================================================
# JSON 是嵌套结构最常见的"文本形态"，网页数据、配置文件都是它
import json

json_text = json.dumps(students, ensure_ascii=False, indent=2)
print(json_text)

# 可以看到：JSON 的 {} 就是 dict，[] 就是 list
# 以后从网上读到的数据，json.loads 之后就是 Python 的嵌套结构


# ============================================================
# 十一、常见陷阱
# ============================================================
# 陷阱 1：键不存在直接报错
#   students[0]["missing"]  ❌ KeyError
#   安全写法：.get("missing", 默认值)

# 陷阱 2：list 索引越界
#   score_list["张三"][10]  ❌ IndexError

# 陷阱 3：修改嵌套值时弄错层级
#   正确：students[0]["score"] = 100
#   错误：students["score"] = 100  ❌ 类型错误

# 陷阱 4：排序忘记 reverse
#   要降序必须写 reverse=True

# 陷阱 5：嵌套列表的浅拷贝
#   copy = matrix[:] 只复制外层，里面的小列表还是共用的
#   需要彻底独立时用 deepcopy：
import copy
matrix_copy = copy.deepcopy(matrix)
