# Day 21 · 异常进阶 知识点速查 (2026.8.16)
# ============================================
# 今天搞懂：try/except/else/finally 四兄弟、raise 主动抛异常、
#           assert 断言、自定义异常类、异常链 raise ... from ...。
# Day 8 学过"文件 I/O + 异常处理"入门，今天是进阶：把异常用透。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。


# ============================================================
# 一、回顾：异常是什么（Day 8 的地基）
# ============================================================
# 异常 = 程序运行到一半"出错了"的信号。比如：
#   1 / 0          → ZeroDivisionError（除零）
#   int("abc")     → ValueError（字符串转数字失败）
#   [1][5]         → IndexError（下标越界）
#   d["不存在"]     → KeyError（字典没有这个键）
#
# 不用 try 接住 → 程序当场崩溃，后面的代码全不执行
# 用 try 接住   → 程序继续跑，不崩溃
#
# 最基础的写法（Day 8 学过）：
#   try:
#       可能出错的代码
#   except 错误类型:
#       出错时执行的代码


# ============================================================
# 二、try / except / else / finally 完整结构（重点）
# ============================================================
# 四兄弟各管一摊：
#   try      圈出"可能出错的代码"
#   except   出错时执行（接住信号）
#   else     没出错时执行（只有"全部成功"才跑）
#   finally  无论出错与否都执行（收尾：关文件、清理）

def demo(a, b):
    try:
        result = a / b                 # 可能出错的代码（除零）
    except ZeroDivisionError:
        return "出错了：除以 0"
    else:
        print(f"计算成功：{a} / {b} = {result}")   # 没出错才执行
        return result
    finally:
        print("收尾：无论如何都会执行")             # 每次都执行

print(demo(10, 2))
# 输出：
# 计算成功：10 / 2 = 5.0
# 收尾：无论如何都会执行
# 5.0

print(demo(10, 0))
# 输出：
# 收尾：无论如何都会执行
# 出错了：除以 0
# 注意顺序：finally 的 print 先执行（在函数真正返回前），外层 print 才打印返回值
# 这正是"finally 在 return 之前跑"的体现
# 收尾：无论如何都会执行

# 【补充】执行流程（务必记牢）：
#   try 没出错：try → else → finally（except 跳过）
#   try 出错了：try 中断 → except → finally（else 跳过）
#   finally 一定执行，不管前面怎么样（return 了也会先跑 finally）

# 【补充】else 有什么用？（新手最容易忽略）
#   try 里的代码如果有好几行，想区分"出错的那行之后还要不要继续"：
#   else 里的代码只在"整个 try 都没出错"时才运行，更精确。
#   也可以不写 else，把成功逻辑直接放 try 末尾——但那样分不清
#   "哪些代码出错会被 except 接住"，逻辑不清。
#   一句话：try 只管"可能出错的部分"，成功的部分放 else。


# ============================================================
# 三、raise：主动抛异常（重点）
# ============================================================
# 大白话：raise = "主动报警"。函数发现参数不合法，主动抛出异常，
#          让调用者知道"你给我的东西不对"，而不是默默返回一个错误值。

def set_age(age):
    # 用法：raise 异常类型("提示信息")
    if age < 0:
        raise ValueError(f"年龄不能为负数，收到 {age}")
    return f"年龄已设置：{age}"

print(set_age(18))       # 年龄已设置：18
# print(set_age(-5))     # ← 会抛 ValueError: 年龄不能为负数，收到 -5

# 【补充】为什么不用 return -1 表示出错？
#   return 一个"约定俗成的错误值"（比如 -1、None）容易和正常结果混淆，
#   而且调用者忘检查就悄悄出错。raise 是"强制"：不接住就崩溃，
#   逼调用者处理，或者让程序早点暴露问题。

# 【补充】raise 不带参数：在 except 里"原样再抛一次"
def f():
    try:
        return int("abc")       # ValueError
    except ValueError:
        print("接住了，但我不处理，原样抛出去")
        raise                   # 不带参数 = 把当前异常继续往外抛

# try:
#     f()
# except ValueError:
#     print("外层接住了 ValueError")
# 输出：
# 接住了，但我不处理，原样抛出去
# 外层接住了 ValueError
# 用途：先记录日志，再交给上层处理。


# ============================================================
# 四、assert：断言（重点）
# ============================================================
# 大白话：assert = "打赌"。断言"这里肯定成立"，
#          如果赌输了（条件为 False），直接抛 AssertionError。
# 用法：assert 条件, "赌输时的提示信息"

def check_positive(x):
    assert x > 0, f"{x} 不是正数"     # 条件 False → AssertionError
    return f"{x} 是正数"

print(check_positive(5))       # 5 是正数
# print(check_positive(-3))    # ← 会抛 AssertionError: -3 不是正数

# 【补充】assert 和 if + raise 的区别？
#   assert 条件, "提示"  ≈  if not 条件: raise AssertionError("提示")
#   但 assert 更简洁，专门表达"这里不该出错"的假设（比如算法中间某值必须是正数）
#   类比：代码的"安检"——检查完放心往下走

# 【大坑】assert 会被 python -O 优化掉！
#   用 python -O 运行程序时，assert 一行会直接消失，不再检查。
#   所以：assert 只用于"开发调试时的自我检查"，
#         不能用于"校验用户输入"（那是正经功能，必须用 if + raise）


# ============================================================
# 五、自定义异常类（重点）
# ============================================================
# 大白话：Python 自带几十种异常（ValueError、TypeError...），
#          但有时候不够用——想要"一看名字就知道错在哪"的异常。
#          自己造一个异常类：继承 Exception 即可。
# 【补充】class 是什么？（Day 32 才系统学，今天只要会用这个句式）
#   class = 定义"类"的关键字，用来"制造一种新的类型"
#   class ScoreError(Exception): 的意思是：
#     ① 造一种叫 ScoreError 的新类型
#     ② 括号里的 Exception = "认 Exception 当父类"（继承）
#        继承 Exception 后，ScoreError 自动成为"异常家族"的一员：
#        能被 raise 抛、能被 except 捕获
#   类比：异常像"错误警报器"，Python 自带几种（ValueError/TypeError...）
#         class 就是"定制警报器"的机器——给错误起个专属名字
#   今天够用的句式（最简单版）：
#     class 名字(Exception):
#         pass
#   下方 AgeError 里的 __init__ 和 self 是"附加数据"的进阶写法，
#   看不懂可以先跳过，做题用简单版即可（Day 32 OOP 会系统讲）

class ScoreError(Exception):
    """分数不合法时抛出"""
    pass        # 什么都不用加，继承就够用

class AgeError(Exception):
    """年龄不合法时抛出"""
    def __init__(self, age, message="年龄不合法"):
        self.age = age              # 额外带上出错的数据
        super().__init__(f"{message}：{age}")

def check_score(score):
    if not 0 <= score <= 100:
        raise ScoreError(f"分数必须在 0~100，收到 {score}")
    return f"分数有效：{score}"

def check_age(age):
    if age < 0 or age > 150:
        raise AgeError(age)         # 自定义异常可以带数据
    return f"年龄有效：{age}"

print(check_score(85))       # 分数有效：85
# print(check_score(150))    # ← 抛 ScoreError: 分数必须在 0~100，收到 150

# 【补充】为什么值得自定义异常？
#   ① 精准捕获：except ScoreError 只接分数错误，不会误接别的 ValueError
#   ② 可读性：看到 raise ScoreError 就知道业务上发生了什么
#   ③ 可扩展：异常类里能带额外数据（age），排查更省事

# 【补充】继承谁？
#   必须继承 Exception（不是 BaseException）！
#   BaseException 的子类还包括 KeyboardInterrupt（Ctrl+C）、SystemExit（退出），
#   它们不是"普通错误"，一般不该被 except 接住。
#   继承 Exception 才是"普通错误"的大家族。


# ============================================================
# 六、异常链：raise ... from ...（进阶）
# ============================================================
# 场景：读取配置文件失败 → 底层抛 FileNotFoundError；
#        你想让调用者看到的是"配置加载失败"（业务角度），
#        但又不想丢掉"到底是哪个文件没找到"的原始信息。
# 解法：捕获底层异常，抛一个新异常，并用 from 把原异常拴上。
# 【补充】用一个比喻理解（快递取货失败）：
#   程序要加载配置 → load_config 像"快递员"去仓库取货（open 文件）
#   仓库不存在（文件不存在）→ 快递员遇到 FileNotFoundError（原始原因）
#   快递员不直接甩给你"仓库编号 404"这种底层细节，
#   他给的正式通知是"您的订单配送失败"（RuntimeError，业务语言）
#   但通知上附了事故单："原因：XX仓库查无此货"（from e 保留原始原因）
#   想深究时翻开通知就能看到底层原因，排查不丢线索
#   一句话：新异常负责"说人话"，from 原异常负责"留证据"
# ------------------------------------------------------------

def load_config(filename):
    try:
        # 【补充】open 的第二个参数是 mode（打开模式），不写默认是 'r'（只读）
        #   open(file, mode='r', encoding=None, ...)
        #   这行等价于 open(filename, 'r', encoding="utf-8")：只读 + UTF-8 编码
        #   常用 mode：'r' 只读（默认）/ 'w' 写入覆盖 / 'a' 追加 / 'x' 新建 / 'b' 二进制（rb/wb）
        #   默认 'r' 时文件不存在会抛 FileNotFoundError → 正好被下面的 except 接住
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        # 用法：raise 新异常 from 原异常 → 异常链
        raise RuntimeError(f"配置加载失败：{filename}") from e

# try:
#     load_config("不存在.txt")
# except RuntimeError as e:
#     print(e)                       # 配置加载失败：不存在.txt
#     print("原始原因：", e.__cause__)  # 原始原因：FileNotFoundError...
# 输出：
# 配置加载失败：不存在.txt
# 原始原因： [Errno 2] No such file or directory: '不存在.txt'

# 【补充】异常链的意义
#   不写 from：Python 也会自动附上"处理异常时又抛出异常"的上下文（__context__）
#   写 from e：明确"新异常是被 e 引起的"（__cause__），语义更清楚
#   排查时从 e.__cause__ 一路往下，能看到完整的"事故现场"
#   Python 报错信息里会显示 "The above exception was the direct cause..." 指向原始异常


# ============================================================
# 七、捕获多个异常 + 捕获顺序（重点）
# ============================================================
# ① 一个 except 接多种：用元组
def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError):      # 括号里列多种，都归这个 except
        return None

print(convert("42"))     # 42
print(convert("abc"))    # None   （ValueError 被接住）
print(convert(None))     # None   （TypeError 被接住）

# ② 多个 except 从上往下匹配：先写具体的，再写宽泛的
def show(container, key):
    try:
        return container[key]
    except KeyError:
        return "键不存在"      # 具体：字典缺键
    except TypeError:
        return "类型不对"      # 具体：container 不支持下标/键是列表
    except Exception:
        return "其他错误"      # 兜底：其他所有普通错误

print(show({"a": 1}, "a"))    # 1
print(show({"a": 1}, "b"))    # 键不存在
print(show([1, 2], "x"))      # 类型不对

# 【大坑】except 顺序写反会怎样？
#   except Exception 写在最前面 → 后面的 KeyError/TypeError 永远轮不到
#   （Exception 是它们的"父类"，先匹配父类，子类就被吞了）
#   规则：先写具体异常，最后才写 Exception 兜底


# ============================================================
# 八、常见陷阱
# ============================================================
# 陷阱 1：裸 except（不写类型）会连 Ctrl+C 都接住
#   except:  = 捕获一切（包括 KeyboardInterrupt、SystemExit）
#   想接"普通错误"请写 except Exception（范围太大也要慎用，会掩盖 bug）
#
# 陷阱 2：else 和 finally 的位置/作用搞混
#   else = 没出错才跑；finally = 无论出错与否都跑
#
# 陷阱 3：assert 校验用户输入
#   python -O 会跳过 assert → 输入校验必须用 if + raise
#
# 陷阱 4：自定义异常没继承 Exception
#   继承 Exception 才是"普通错误"；继承 BaseException 会连系统级异常混一起
#
# 陷阱 5：raise 不带信息
#   raise ValueError 不如 raise ValueError("参数 xxx 不能为负") 好排查
#
# 陷阱 6：finally 里的 return 会覆盖 try 的 return
#   def f():
#       try:
#           return 1
#       finally:
#           return 2    # 结果返回 2！finally 的 return 赢了
#   finally 是"收尾"用的，别在里面写 return
#   【补充】finally 里不写 return 写什么？→ 写"收尾动作"（普通语句）：
#     def f():
#         try:
#             return 1
#         finally:
#             print("收尾中...")   # ✅ 只做收尾：打印、关文件、清理资源
#     f() 返回 1（finally 不影响返回值）
#   口诀：finally 是"收拾东西走人"，不是"重新决定带什么走"


# ============================================================
# 九、例题精讲（看懂了再去做练习）
# ============================================================

# ------------------------------------------------------------
# 例题 1：除法函数——除零返回 None，正常才打印成功
# 思路：try/except 接除零，else 放成功逻辑
# ------------------------------------------------------------
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        print(f"{a} / {b} = {result}")   # 只有没出错才打印
        return result
    finally:
        print("计算结束")                  # 无论成败都打印

print(safe_divide(10, 2))
# 输出：
# 10 / 2 = 5.0
# 计算结束
# 5.0
print(safe_divide(1, 0))
# 输出：
# 计算结束
# None

# 关键点：else 只在成功时跑；finally 永远跑；return 在 finally 之后才真正生效

# ------------------------------------------------------------
# 例题 2：输入校验——年龄不合法主动 raise
# 思路：if 判断 + raise ValueError(带信息)
# ------------------------------------------------------------
def input_age(age_text):
    age = int(age_text)                 # 转数字，转不了会抛 ValueError
    if age < 0:
        raise ValueError(f"年龄不能为负：{age}")
    if age > 150:
        raise ValueError(f"年龄过大：{age}")
    return age

print(input_age("18"))     # 18
# print(input_age("-1"))   # ← ValueError: 年龄不能为负：-1
# print(input_age("abc"))  # ← ValueError（int 转不了）

# 关键点：函数"入口校验"用 raise，让问题在源头暴露

# ------------------------------------------------------------
# 例题 3：自定义异常 + assert 组合
# 思路：业务错误用自定义异常，逻辑假设用 assert
# ------------------------------------------------------------
class MoneyError(Exception):
    """金额不合法"""
    pass

def withdraw(balance, amount):
    assert amount >= 0, "取款金额不能为负"          # 逻辑假设：断言
    if amount > balance:
        raise MoneyError(f"余额不足：余额 {balance}，想取 {amount}")  # 业务错误
    return balance - amount

print(withdraw(100, 30))     # 70
# print(withdraw(100, -5))   # ← AssertionError: 取款金额不能为负
# print(withdraw(10, 50))    # ← MoneyError: 余额不足：余额 10，想取 50

# 关键点：assert 管"代码不该出错"；raise 管"业务上确实出错"

# ------------------------------------------------------------
# 例题 4：异常链——底层错误包成业务错误
# 思路：except 里 raise 新异常 from 原异常
# ------------------------------------------------------------
class DataLoadError(Exception):
    """数据加载失败"""
    pass

def load_data(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    # 【补充】OSError 是什么？（Operating System Error，操作系统错误）
    #   = 和"操作系统打交道"出错时的一类异常的"总爸爸"（父类）
    #   open() 文件相关的错误几乎都是它家族：
    #     FileNotFoundError（文件不存在）/ PermissionError（没权限）
    #     IsADirectoryError（把目录当文件打开）/ FileExistsError（文件已存在）
    #     ConnectionError（网络连接问题）...
    #   这里写 except OSError 比 except Exception 好：
    #     精确——只接文件/系统类错误，不会把代码里其他 bug（如 NameError）也吞掉
    #   经验法则：能写多具体就写多具体（FileNotFoundError → OSError → Exception）
    except OSError as e:
        raise DataLoadError(f"无法加载数据：{path}") from e

try:
    load_data("没有这个文件.txt")
except DataLoadError as e:
    print("业务错误：", e)
    print("原始原因：", type(e.__cause__).__name__)   # FileNotFoundError
# 输出：
# 业务错误： 无法加载数据：没有这个文件.txt
# 原始原因： FileNotFoundError

# 关键点：from e 保留"事故现场"，外层只看业务错误也不丢线索


# ============================================================
# 十、今天总结（一图流）
# ============================================================
# try/except  接住异常，程序不崩
# else        没出错才执行（成功逻辑）
# finally     无论出错与否都执行（收尾）
# raise       主动报警（参数不合法等）
# assert      打赌式检查（开发期假设，别用于输入校验）
# 自定义异常   继承 Exception，错误有名字、可精准捕获
# raise ... from ...   异常链，保留原始原因
#
# 明天 Day 22：编码与 bytes（ASCII/Unicode/UTF-8/GBK、str vs bytes）
