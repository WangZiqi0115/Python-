# Day 5 · 字符串方法 知识点速查 (2026.7.31)
# ============================================
# 保留此文件，以后忘了回来查。
#


# ============================================================
# 一、字符串的特性
# ============================================================
# 字符串是"不可变"的——任何修改操作都会返回新字符串，原字符串不变
s = "hello"
s.upper()            # "HELLO"
print(s)             # "hello"   原字符串没变
s = s.upper()        # 只有重新赋值，s 才会指向新字符串


# ============================================================
# 二、大小写转换
# ============================================================
s = "Hello World"

s.lower()            # "hello world"     全转小写
s.upper()            # "HELLO WORLD"     全转大写
s.capitalize()       # "Hello world"     首字母大写，其余小写
s.title()            # "Hello World"     每个单词首字母大写
s.swapcase()         # "hELLO wORLD"     大小写互换

# 应用：忽略大小写比较
"Python" == "python"              # False
"Python".lower() == "python".lower()  # True


# ============================================================
# 三、查找与判断
# ============================================================
s = "hello python world"

# 查找子串位置
s.find("python")         # 6   返回第一次出现的索引
s.find("java")           # -1  没找到返回 -1（不报错）
s.index("python")        # 6   和 find 一样，但没找到会报错

# 判断开头/结尾
s.startswith("hello")    # True
s.endswith("world")      # True

# 判断内容类型
"123".isdigit()          # True   是否全是数字
"abc".isalpha()          # True   是否全是字母
"abc123".isalnum()       # True   是否全是字母或数字
"   ".isspace()          # True   是否全是空白
"Hello".isupper()        # False  是否全是大写
"hello".islower()        # True   是否全是小写


# ============================================================
# 四、切割与拼接
# ============================================================
# split() — 按分隔符拆成列表
"a,b,c".split(",")        # ["a", "b", "c"]
"hello world".split()     # ["hello", "world"]  默认按空白拆
"a,b,c,d".split(",", 2)  # ["a", "b", "c,d"]   只拆前 2 个

# join() — 把列表拼回字符串（反过来）
",".join(["a", "b", "c"])     # "a,b,c"
" ".join(["hello", "world"])  # "hello world"

# splitlines() — 按换行拆
"line1\nline2\nline3".splitlines()  # ["line1", "line2", "line3"]


# ============================================================
# 五、替换与去除空白
# ============================================================
# replace() — 替换子串
"hello world".replace("world", "python")  # "hello python"
"a,b,c".replace(",", " | ")               # "a | b | c"

# strip() — 去除首尾空白（最常用）
"  hello  ".strip()            # "hello"
"\n\t hello \n".strip()       # "hello"  去掉了换行和制表符

# lstrip() / rstrip() — 只去左边 / 只去右边
"  hello  ".lstrip()           # "hello  "
"  hello  ".rstrip()           # "  hello"

# strip() 也可以去掉指定字符
"---hello---".strip("-")       # "hello"


# ============================================================
# 六、统计与填充
# ============================================================
# count() — 统计子串出现次数
"hello hello world".count("hello")   # 2
"banana".count("na")                 # 2

# len() — 字符串长度（和列表一样）
len("hello")                         # 5

# 填充对齐
"hello".center(11)          # "   hello   "   居中对齐
"hello".ljust(10)           # "hello     "    左对齐
"hello".rjust(10)           # "     hello"    右对齐
"42".zfill(5)              # "00042"         左侧补零


# ============================================================
# 七、字符串格式化的三种方式
# ============================================================
name = "示其"
age = 18
score = 95.5

# 方式 1：f-string（最推荐，Python 3.6+）
f"我叫{name}，今年{age}岁，考了{score}分"
# "我叫示其，今年18岁，考了95.5分"

# 方式 2：.format()
"我叫{}，今年{}岁".format(name, age)

# 方式 3：% 格式化（旧写法，能看懂就行）
"我叫%s，今年%d岁" % (name, age)

# f-string 进阶用法
f"{score:.1f}"              # "95.5"   保留一位小数
f"{score:06.1f}"            # "0095.5" 补零到 6 位
name = "示其"
f"{name:>10}"               # "        示其"  右对齐宽度10
f"{name:<10}"               # "示其        "  左对齐宽度10
f"{name:^10}"               # "    示其    "  居中对齐宽度10


# ============================================================
# 八、综合应用场景
# ============================================================

# 场景 1：清洗用户输入
user_input = "   Zhang San   \n"
cleaned = user_input.strip().lower()   # "zhang san"

# 场景 2：解析 CSV 数据
line = "张三,95,重庆\n"
parts = line.strip().split(",")        # ["张三", "95", "重庆"]

# 场景 3：生成 SQL 查询占位符
ids = [1, 2, 3]
placeholders = ", ".join(["?"] * len(ids))  # "?, ?, ?"

# 场景 4：检测文件扩展名
filename = "data.csv"
if filename.endswith(".csv"):
    print("这是一个 CSV 文件")

# 场景 5：格式化输出表格
print(f"{'姓名':<10}{'分数':<10}{'等级':<10}")
print(f"{'张三':<10}{95:<10}{'优秀':<10}")
print(f"{'李四':<10}{87:<10}{'良好':<10}")
# 姓名       分数       等级
# 张三       95        优秀
# 李四       87        良好


# ============================================================
# 九、常见陷阱
# ============================================================

# 陷阱 1：字符串不可变——方法不会修改原字符串
s = "hello"
s.upper()              # 返回 "HELLO"，但 s 还是 "hello"
print(s)               # "hello"
# 必须重新赋值：
s = s.upper()

# 陷阱 2：split 和 join 是反操作
s = "a,b,c"
lst = s.split(",")     # ["a", "b", "c"]
back = ",".join(lst)   # "a,b,c"

# 陷阱 3：链式调用（一行连续调多个方法）
text = "  Hello World  "
result = text.strip().lower().replace(" ", "_")
print(result)            # "hello_world"
# 从前往后执行：去空白 → 转小写 → 替换空格
