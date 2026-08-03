# Day 8 · 文件 I/O + 异常处理 知识点速查 (2026.8.3)
# ============================================
# 今天学会读写文件，以及让程序出错时不崩溃。
#


# ============================================================
# 一、打开和读取文件（基础）
# ============================================================
# open(文件名, 模式) 打开文件
# 读取模式：r = read（默认）、w = write（写）、a = append（追加）

# 读取整个文件内容
f = open("data.txt", "r")     # 打开文件（默认 r 可省略）
content = f.read()            # 读全部内容，返回字符串
f.close()                     # 用完必须关闭！
print(content)

# 逐行读取
f = open("data.txt", "r")
for line in f:                # 文件对象可以直接遍历，每行一个字符串
    print(line.strip())       # strip() 去掉每行末尾的换行符
f.close()

# readlines()：一次读成列表
f = open("data.txt", "r")
lines = f.readlines()         # ["第一行\n", "第二行\n", ...]
f.close()


# ============================================================
# 二、with 语句（推荐写法！）
# ============================================================
# 手写 f.close() 容易忘，忘了会导致文件被占着
# with 会在代码块结束时自动关闭文件，不用手动 close

with open("data.txt", "r") as f:
    content = f.read()
# 到这里文件已经自动关闭了

# 日常最常用写法：
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# encoding="utf-8"：指定中文编码，读中文文件必加！


# ============================================================
# 三、写入文件
# ============================================================
# 模式 w：覆盖写入（文件不存在会创建，存在会清空重写）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")       # write 不会自动换行，要自己加 \n
    f.write("第二行\n")

# 模式 a：追加写入（不清空原文件，在末尾加）
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("第三行\n")

# 写多行：用循环或 join
lines = ["张三,95", "李四,82"]
with open("output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
    # 或者：f.writelines([l + "\n" for l in lines])


# ============================================================
# 四、异常处理 try / except（重点）
# ============================================================
# 异常 = 程序运行时报的错（你见过很多：KeyError、ValueError...）
# 没有处理的异常会让程序崩溃。try/except 可以"接住"它

# 基本格式：
try:
    # 可能出错的代码
    num = int("abc")          # 这行会报 ValueError
except ValueError:
    # 出错后执行这里的代码
    print("转换失败！")
# 程序不会崩溃，继续往下走

# 示例：打开不存在的文件
try:
    with open("不存在.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在，请检查文件名")

# 多个 except：不同类型的错误分开处理
try:
    num = int(input("输入数字："))
    result = 10 / num
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以 0！")

# 捕获所有异常（尽量少用，先精准捕获）
try:
    risky_code()
except Exception as e:
    print("出错了：", e)


# ============================================================
# 五、try / except / else / finally
# ============================================================
# else：没有异常时执行
# finally：无论有没有异常都执行（通常用来收尾）

try:
    num = int("123")
except ValueError:
    print("转换失败")
else:
    print("转换成功：", num)      # 没出错才走这里
finally:
    print("这段无论如何都会执行")

# 完整流程：
# try 出错 → except 执行 → finally 执行
# try 没出错 → else 执行 → finally 执行


# ============================================================
# 六、常见文件操作模式
# ============================================================

# 模式 1：读取所有行并清洗
with open("scores.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
    # 去掉了每行的换行符和空行

# 模式 2：读取 CSV 并解析
with open("students.csv", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        # parts = ["张三", "95", "重庆"]  ← Day 5 学的！
        print(parts)

# 模式 3：边读边写（处理大文件不占内存）
with open("input.txt", "r", encoding="utf-8") as fin:
    with open("output.txt", "w", encoding="utf-8") as fout:
        for line in fin:
            fout.write(line.strip() + "\n")

# 模式 4：安全的读文件（带异常处理）
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []               # 文件不存在返回空列表，不崩溃
    except Exception as e:
        print("读取出错：", e)
        return []


# ============================================================
# 七、把函数、异常、文件串起来
# ============================================================
# 实战：统计文件中每个单词出现次数

def count_words(filename):
    """读取文件并统计词频，返回字典"""
    freq = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                words = line.strip().lower().split()
                for word in words:
                    freq[word] = freq.get(word, 0) + 1
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return {}
    return freq

# 调用：
# result = count_words("article.txt")
# print(result)


# ============================================================
# 八、常见陷阱
# ============================================================

# 陷阱 1：忘写 encoding="utf-8" → 读中文可能乱码或报错
# 解决办法：读写中文文件都加 encoding="utf-8"

# 陷阱 2：write 不会自动换行
# "第一行" + "第二行" 会连在一起
# 解决：手动加 "\n"

# 陷阱 3：w 模式会清空原文件！
# 想保留原内容追加，用 a 模式

# 陷阱 4：文件用完后没关闭
# 用 with 自动关闭，不要裸 open()

# 陷阱 5：except 太宽泛
# 不要直接 except:（捕获所有），尽量写具体异常类型
