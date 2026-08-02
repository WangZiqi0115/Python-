# Day 8 · 函数专题 知识点速查 (2026.8.2)
# ============================================
# 前七天的坑：返回值、参数、作用域、函数作为参数
# 今天一次性解决。
#


# ============================================================
# 一、函数是什么
# ============================================================
# 函数 = 一段可重复使用的代码块
# 你已经写过很多了：problem1()、analyze_scores()、add_contact() 都是函数

def greet():
    print("你好")

# 调用：函数名 + 括号
greet()          # 你好

# 关键记忆：括号 = "执行"
greet            # 只是函数的"名字"，不执行
greet()          # 真正执行函数体

# 这也解释了为什么 word.lower 必须加括号：
# lower 是字符串自带的函数，word.lower 是"函数名"，word.lower() 才是执行


# ============================================================
# 二、参数（重点：搞清变量名）
# ============================================================
# 你犯过"变量名搞混"的错：scores vs score、analyze_scores vs scores
# 记住：函数括号里的参数名，就是函数内部使用的名字

def analyze_scores(scores):      # scores 是函数内部的名字
    max_score = max(scores)      # 内部用它
    return max_score

# 调用时传什么，scores 就是什么
analyze_scores([70, 55, 90])     # scores = [70, 55, 90]
analyze_scores([1, 2, 3])        # scores = [1, 2, 3]

# 参数名是函数"内部"的名字，和外部变量无关！
def add(x, y):
    return x + y

a = 10
b = 20
add(a, b)        # 外部 a、b 的值传入，内部 x=a=10, y=b=20
add(5, 7)        # 内部 x=5, y=7

# 所以遍历字典时也要搞清变量名：
scores = {"张三": 95, "李四": 82}
for name, score in scores.items():   # name 是键，score 是值
    if score >= 90:                  # 判断的是"每个学生的分数"
        print(name)


# ============================================================
# 三、返回值（重点：哪些有、哪些没有）
# ============================================================
# return 的作用：把结果"递"给调用者
def add(a, b):
    return a + b

result = add(3, 5)    # result = 8，函数把结果递出来了

# 没有 return 的函数：返回 None
def do_nothing():
    print("做了一点事")

result = do_nothing()  # result = None！

# 你踩过的坑：方法有没有返回值？
# 修改原对象的操作（append/remove/sort/clear）→ 返回 None
# 生成新对象的操作（pop/copy/sorted/切片）→ 有返回值

lst = [1, 2, 3]
r1 = lst.append(4)      # r1 = None！append 只是修改 lst，不递东西
r2 = lst.pop()          # r2 = 4！pop 删除并把值递出来
r3 = sorted(lst)        # r3 = 新排序列表
r4 = lst.sort()         # r4 = None！sort 修改 lst，不递东西

# 赋值语句也不返回东西！
# 错误：new_list = lst.append(4)   → new_list 是 None
# 正确：lst.append(4); return lst  → 先执行操作，再把修改后的列表返回


# ============================================================
# 四、参数的三种类型
# ============================================================

# 1. 位置参数（按顺序传）
def info(name, age, city):
    return f"{name}，{age}岁，{city}"

info("示其", 18, "重庆")      # 按顺序：name=示其, age=18, city=重庆

# 2. 关键字参数（按名字传，顺序可打乱）
info(city="重庆", name="示其", age=18)   # 结果一样

# 3. 默认参数（不传时用默认值）
def greet2(name, greeting="你好"):
    return f"{greeting}，{name}"

greet2("示其")              # "你好，示其"（greeting 用默认值）
greet2("示其", "早上好")     # "早上好，示其"（覆盖默认值）

# ⚠️ 默认参数陷阱（你 Day 3 见过）
def bad(lst=[]):        # ❌ 默认列表只创建一次
    lst.append(1)
    return lst

print(bad())            # [1]
print(bad())            # [1, 1] ← 不是 [1]！

def good(lst=None):     # ✅ 用 None 占位
    if lst is None:
        lst = []
    lst.append(1)
    return lst


# ============================================================
# 五、局部变量 vs 全局变量
# ============================================================
# 函数内部定义的变量是"局部的"——只在函数内有效
# 函数外部的变量是"全局的"——到处都能读

x = 10                # 全局变量

def change_x():
    x = 20            # 函数内部新定义了一个局部 x，和全局 x 无关
    return x

print(change_x())     # 20（局部 x）
print(x)              # 10（全局 x 没变）

# 想修改全局变量？用 global（不推荐，了解即可）
y = 5
def add_global():
    global y
    y += 1

add_global()
print(y)              # 6

# 函数内部读取全局变量是允许的
x = 10
def read_x():
    return x          # ✅ 读全局没问题

print(read_x())       # 10


# ============================================================
# 六、函数作为参数传递（你之前问过 key= 的原理）
# ============================================================
# 函数名本身可以当作值传递——不加括号！

# 例 1：len 作为 key
words = ["python", "java", "c"]
sorted(words, key=len)       # ["c", "java", "python"]

# 例 2：自定义函数作为 key
def get_score(student):
    return student[1]

students = [("张三", 95), ("李四", 87)]
sorted(students, key=get_score)   # 传函数名，不加括号！

# 例 3：lambda 一行定义函数（等价于 get_score）
sorted(students, key=lambda x: x[1])

# 例 4：max/min 也可以用
scores = {"张三": 95, "李四": 82}
max(scores, key=scores.get)   # "张三"

# 原理：sorted/max 内部会"自动调用"你给的函数
# 你传的是"技能"，它来按技能执行


# ============================================================
# 七、高阶函数：map / filter（了解）
# ============================================================
# map(函数, 列表)：对每个元素调用函数，返回结果
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)        # [1, 4, 9, 16]

# filter(函数, 列表)：按条件筛选元素
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)           # [2, 4]

# 等价写法（列表推导式）
[x**2 for x in nums]          # [1, 4, 9, 16]
[x for x in nums if x % 2 == 0]  # [2, 4]

# 实际写代码时，推导式更常用也更直观


# ============================================================
# 八、函数返回多个值（元组解包）
# ============================================================
def analyze_scores(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg = sum(scores) / len(scores)
    return max_score, min_score, avg     # 本质是返回一个元组

result = analyze_scores([70, 55, 90])
print(result)               # (90, 55, 71.67)
print(type(result))         # <class "tuple">

# 解包接收
mx, mn, avg = analyze_scores([70, 55, 90])
print(mx, mn, avg)          # 90 55 71.67


# ============================================================
# 九、*args 和 **kwargs（进阶，了解即可）
# ============================================================
# *args：接收任意多个位置参数，打包成元组
def my_sum(*args):
    return sum(args)

my_sum(1, 2, 3)            # 6
my_sum(1, 2, 3, 4, 5)      # 15

# **kwargs：接收任意多个关键字参数，打包成字典
def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

show_info(name="示其", age=18)
# name: 示其
# age: 18


# ============================================================
# 十、你过去的坑 → 今天的对策
# ============================================================

# 坑 1：忘加括号（word.lower、parts[4].strip）
# 对策：只要想"让函数做事"，就加 ()

# 坑 2：append/remove/赋值没有返回值
# 对策：先执行操作，再 return 修改后的对象

# 坑 3：变量名搞混（scores vs score）
# 对策：遍历时解包变量名要对应：for key, value in d.items()

# 坑 4：字典覆盖（contacts = {...}）
# 对策：修改字典用 d[key] = value，不要整体重新赋值

# 坑 5：索引从 0 数
# 对策：第 n 个元素 → 索引 n-1

# 坑 6：函数参数是内部名字
# 对策：定义函数时想好内部变量名，调用时只关心传什么值
