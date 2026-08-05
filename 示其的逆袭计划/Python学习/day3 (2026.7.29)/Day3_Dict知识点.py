# Day 3 · Dict 字典 知识点速查 (2026.7.29)
# ============================================
# 保留此文件，以后忘了回来查。
#


# ============================================================
# 一、字典是什么
# ============================================================
# 字典是"键值对"的集合——通过 key 找 value，像查真字典一样
# key 必须是不可变的（字符串、数字、元组），value 可以是任何类型
# Python 3.7+ 字典保持插入顺序，但不要过度依赖

# 创建字典
d1 = {"name": "示其", "age": 18, "city": "重庆"}
d2 = {}                         # 空字典
d3 = dict(name="示其", age=18)  # 用 dict() 创建
d4 = dict([("a", 1), ("b", 2)]) # 从元组列表创建
d5 = dict(zip(["a","b"], [1,2])) # 从 zip 创建

# 【补充】{"name": "示其"} 和 dict(name="示其") 效果一样，但有限制：
#   dict(key=value) 要求 key 必须是合法的变量名（无空格、不能数字开头、不能是关键字）
#   {"first name": "示其"} 可以，dict(first name="示其") 会报错
#   日常建议直接用 {} 最省心


# ============================================================
# 二、访问与取值
# ============================================================
d = {"name": "示其", "age": 18, "city": "重庆"}

# 方式 1：方括号取值（key 不存在会报错 KeyError）
d["name"]          # "示其"
# d["score"]        ❌ KeyError！

# 方式 2：get() 安全取值
d.get("name")      # "示其"
d.get("score")     # None       ← 不会报错
d.get("score", 0)  # 0          ← 指定默认值

# 方式 3：setdefault() — 取值，如果 key 不存在则设默认值再返回
d.setdefault("name", "未知")    # "示其"（已存在，返回原值）
d.setdefault("score", 0)        # 0（不存在，设 score=0 并返回 0）
# 注意：setdefault 会修改原字典！get 不会

# 判断 key 是否存在
"name" in d        # True
"score" in d       # True（刚才 setdefault 添加了）


# ============================================================
# 三、增删改
# ============================================================
d = {"name": "示其", "age": 18}

# 添加 / 修改（同一个语法）
d["city"] = "重庆"     # 新增
d["age"] = 19          # 修改

# update() — 合并另一个字典
d.update({"score": 95, "city": "北京"})  # 新增 score，修改 city
# {"name": "示其", "age": 19, "city": "北京", "score": 95}

# Python 3.9+ 还可以用 | 运算符合并（了解即可）
# d = d | {"grade": "A"}

# 删除
del d["age"]          # 删除指定键值对
val = d.pop("score")  # 删除并返回被删的值，val = 95
d.pop("不存在的key", "默认值")   # 防止 KeyError

# popitem() — 删除并返回最后一对（了解）
last = d.popitem()    # ("city", "北京")

# clear() — 清空
d.clear()             # {}


# ============================================================
# 四、遍历字典
# ============================================================
d = {"name": "示其", "age": 18, "city": "重庆"}

# 遍历 key
for k in d:
    print(k)           # name  age  city

# 遍历 value
for v in d.values():
    print(v)

# 遍历 key 和 value（最常用）
for k, v in d.items():
    print(k, v)


# ============================================================
# 五、常用方法速查
# ============================================================
d = {"a": 1, "b": 2, "c": 3}

d.keys()              # dict_keys(["a", "b", "c"])
d.values()            # dict_values([1, 2, 3])
d.items()             # dict_items([("a",1), ("b",2), ("c",3)])
d.get("a")            # 1
d.get("x", 0)         # 0       没找到返回默认值
d.setdefault("d", 4)  # 4       不存在就设默认值
d.update({"e": 5})    # 合并
d.pop("a")            # 1       删除并返回
d.pop("x", None)      # None    不会报错


# ============================================================
# 六、字典推导式
# ============================================================
# 和列表推导式类似，但用 {} 包起来，且有冒号

# 基本
{x: x**2 for x in range(5)}      # {0:0, 1:1, 2:4, 3:9, 4:16}

# 加条件
{x: x**2 for x in range(10) if x % 2 == 0}

# 遍历已有字典生成新字典
d = {"a": 1, "b": 2, "c": 3}
{k: v*10 for k, v in d.items()}   # {"a": 10, "b": 20, "c": 30}

# 反转 key 和 value
{v: k for k, v in d.items()}      # {1:"a", 2:"b", 3:"c"}

# 双 for 循环
{x: y for x in [1,2] for y in ["a","b"]}
# {1: "b", 2: "b"}  注意：每个 key 只保留最后一个 value


# ============================================================
# 七、嵌套字典
# ============================================================
# 字典的 value 可以是另一个字典——这就是嵌套

students = {
    "001": {"name": "张三", "score": 95, "city": "北京"},
    "002": {"name": "李四", "score": 87, "city": "上海"},
    "003": {"name": "王五", "score": 92, "city": "重庆"}
}

# 访问嵌套数据
students["001"]["name"]        # "张三"
students["002"]["score"]       # 87

# 遍历嵌套字典
for sid, info in students.items():
    print(f"{sid}: {info["name"]} — {info["score"]}分")

# 列表套字典（也很常见）
scores = [
    {"name": "张三", "score": 95},
    {"name": "李四", "score": 87}
]
scores[0]["name"]              # "张三"


# ============================================================
# 八、dict.fromkeys() 去重（复习与深入）
# ============================================================
# 用法1：一键多值赋默认值
dict.fromkeys(["a", "b", "c"], 0)
# {"a": 0, "b": 0, "c": 0}

# 用法2：列表去重并保持顺序（你学过的）
items = [3, 1, 2, 1, 3, 4]
list(dict.fromkeys(items))     # [3, 1, 2, 4]

# 注意：第二个参数如果是可变对象要小心！
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
print(d)          # {"a": [1], "b": [1]}  两个共用一个列表！


# ============================================================
# 九、defaultdict — 带默认值的字典（扩展）
# ============================================================
# 普通 dict 取不存在的 key 会报错或需要 get()
# defaultdict 会自动给不存在的 key 一个默认值

from collections import defaultdict

# 默认类型为 int，不存在的 key 自动初始化为 0
freq = defaultdict(int)
freq["apple"] += 1
freq["apple"] += 1
freq["banana"] += 1
print(dict(freq))   # {"apple": 2, "banana": 1}

# 默认类型为 list
groups = defaultdict(list)
groups["A"].append("张三")
groups["A"].append("李四")
groups["B"].append("王五")
print(dict(groups)) # {"A": ["张三", "李四"], "B": ["王五"]}


# ============================================================
# 十、经典应用场景
# ============================================================

# 场景 1：词频统计（你用 get 做过了，看看 defaultdict 版）
from collections import defaultdict
# 从 collections 模块导入 defaultdict
text = "apple banana apple orange banana apple"
# 准备一段文本，apple×3, banana×2, orange×1
freq = defaultdict(int)
# 创建 defaultdict，指定默认类型为 int（默认值为 0）
for word in text.split():
# text.split() 把字符串按空格拆成列表，逐个取单词
    freq[word] += 1
# 相当于 freq[word] = freq[word] + 1
# 第一次遇到某单词时，defaultdict 自动设为 0，再 +1
print(dict(freq))    # {"apple": 3, "banana": 2, "orange": 1}
# dict(freq) 把 defaultdict 转成普通字典后打印

# --- 和 get() 写法的对比 ---
# 下面这段代码和上面的 defaultdict 版本效果完全一样
# text2 = "apple banana apple orange banana apple"
# freq2 = {}
# for word in text2.split():
#     freq2[word] = freq2.get(word, 0) + 1
# print(freq2)  # {"apple": 3, "banana": 2, "orange": 1}
# 
# 区别：defaultdict 省去了每次写 .get(word, 0) 的步骤
# 逻辑完全一样——"不存在就取 0，然后 +1"
# 

# 场景 2：用字典做映射表
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
print(f"2月有{month_days[2]}天")

# 场景 3：分组
students = ["张三", "安娜", "王五", "艾米", "李四"]
group = defaultdict(list)
for name in students:
    first_char = name[0]
    group[first_char].append(name)
print(dict(group))
# {"张": ["张三"], "安": ["安娜"], "王": ["王五"], "艾": ["艾米"], "李": ["李四"]}

# 场景 4：用字典实现 switch/case（Python 没有 switch）
def operate(op, a, b):
    operations = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else None
    }
    return operations.get(op, "未知操作")

print(operate("add", 10, 5))    # 15
print(operate("mul", 10, 5))    # 50

# 场景 5：用字典记录多个属性
student = {
    "name": "示其",
    "scores": [95, 87, 92],
    "info": {"age": 18, "city": "重庆"}
}
print(student["scores"][0])         # 95
print(student["info"]["city"])      # 重庆


# ============================================================
# 十一、字典 vs 列表 对比
# ============================================================
# 列表适合：按顺序存、按位置取
# 字典适合：按名字存、按名字取

# 用列表存学生分数
scores_list = [95, 87, 92]          # 不知道是谁的分数

# 用字典存
scores_dict = {"张三": 95, "李四": 87, "王五": 92}

# 查找张三的分数
# 列表：得先知道张三在索引几，或者单独维护一个名字列表
# 字典：scores_dict["张三"] 一步到位

# 使用建议：
# 顺序访问、索引访问 → 列表
# 按名字查找、一对一映射 → 字典


# ============================================================
# 十二、常见陷阱
# ============================================================

# 陷阱 1：可变对象作为默认值
def add_student(name, lst=[]):   # ❌ 默认列表只创建一次
    lst.append(name)
    return lst

print(add_student("张三"))       # ["张三"]
print(add_student("李四"))       # ["张三", "李四"]   ← 不是 ["李四"]！

# 正确做法：
def add_student_safe(name, lst=None):
    if lst is None:
        lst = []
    lst.append(name)
    return lst

# 陷阱 2：遍历时删除
d = {"a": 1, "b": 2, "c": 3}
# for k in d:          # ❌ 遍历时不能修改字典大小
#     if k == "b":
#         del d[k]     # RuntimeError！

# 正确做法：遍历 list(d.keys()) 副本
for k in list(d.keys()):
    if k == "b":
        del d[k]
print(d)               # {"a": 1, "c": 3}

# 陷阱 3：多个键引用同一个可变 value
d = {"a": [], "b": []}           # ✅ 两个独立列表
d["a"].append(1)
print(d)                         # {"a": [1], "b": []}
