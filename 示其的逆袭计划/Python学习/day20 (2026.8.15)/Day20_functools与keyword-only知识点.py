# Day 20 · functools 与 keyword-only 知识点速查 (2026.8.15)
# ============================================
# 今天搞懂：keyword-only 参数（* 后面的必关键字参数）+ functools 四大工具
#           （reduce / partial / lru_cache / cmp_to_key）。
# 昨天学的装饰器今天还会见到老朋友：functools.wraps 就是 functools 模块里的。
#
# 本文件是速查手册，想动手验证时把代码复制到"代码测试专用.py"里运行。


# ============================================================
# 一、为什么需要 functools 和 keyword-only
# ============================================================
# 【名字怎么来的？】functools = function（函数）+ tools（工具），直译"函数工具"
# functools 是 Python 标准库模块，专门给函数"加能力"：
#   - functools.wraps    保留函数身份证（昨天学过）
#   - functools.reduce   把序列"卷"成一个值
#   - functools.partial  提前固定一部分参数
#   - functools.lru_cache 记住算过的结果（缓存）
#   - functools.cmp_to_key 把旧式比较函数变成 sorted 的 key
#
# 【名字怎么来的？】keyword-only 直译"仅限关键字"：
#   keyword（关键字）这里指"关键字参数"的写法，即调用时写 名字=值
#   （注意：不是 if/def/for 那种保留字 reserved keyword，别混了）
#   only（仅仅）= 只允许这一种传法，禁止按位置传
# keyword-only（必关键字参数）是 Python 函数定义里的一个语法：
#   在参数列表里写一个单独的 *，它后面的参数"只能用关键字传"。
#   比如 def f(a, b, *, c)：调用时 c 必须写成 c=xxx。
#   作用：参数多了不容易搞混，代码一看就懂。


# ============================================================
# 二、keyword-only：* 后面的必关键字参数（重点）
# ============================================================
# 语法：def 函数名(普通参数..., *, 只能关键字传的参数...)
# 注意：这个 * 不是 *args，它不收集参数，只是"一堵墙"：
#       墙前面的参数可以按位置传，墙后面的必须用 名字=值 传。

# 例子：订奶茶
def order_milk_tea(base, size, *, sugar="七分糖", ice="正常冰"):
    # base 和 size 可以按位置传；sugar 和 ice 必须用关键字传
    return f"{size}杯{base}，{sugar}，{ice}"

print(order_milk_tea("珍珠奶茶", "中"))          # 中杯珍珠奶茶，七分糖，正常冰
print(order_milk_tea("珍珠奶茶", "大", sugar="无糖", ice="去冰"))  # 关键字传，合法
# print(order_milk_tea("珍珠奶茶", "大", "无糖", "去冰"))  # ← 会报错！
# TypeError: order_milk_tea() takes 2 positional arguments but 4 were given
# 因为 sugar 和 ice 在 * 后面，禁止按位置传

# 【补充】这个 * 和 *args 有什么区别？
#   def f(*args)：*args 把"所有多余位置参数"打包成元组 → 参数个数不固定
#   def f(a, *, b)：单独一个 * 不打包任何东西，只是"分隔符"，告诉 Python：
#       后面的参数 b 只能关键字传
#   一句话：*args 是"收参数的网兜"；单独 * 是"写着'后面必须用关键字'的牌子"

# 【补充】* 后面的参数可以有默认值，也可以没有默认值：
def f1(*, a, b=10):      # a 必填（无默认值），b 可选（有默认值）
    return a + b
print(f1(a=1))           # 11        # 只传 a，b 用默认值
print(f1(a=1, b=2))      # 3         # 两个都传

# 【补充】* 前面也可以写 *args（两者可以同时出现）：
def f2(name, *args, **kwargs):
    # name 按位置；多余位置参数进 args；多余关键字参数进 kwargs
    return name, args, kwargs
print(f2("示其", 1, 2, hobby="编程"))
# 输出：('示其', (1, 2), {'hobby': '编程'})
# 注意：kwargs 里的参数天生就只能关键字传（字典就是名字=值），
#       * 后面的参数本质上也走 kwargs 这条"关键字通道"。

# keyword-only 有什么用？
#   ① 参数一多，按位置传容易传错（比如把"糖"传给"冰"）
#   ② 强制调用者写清楚参数名，代码可读性更高
#   ③ 未来加参数不破坏已有调用（新参数放 * 后面，老调用不受影响）


# ============================================================
# 三、functools.reduce：把序列"卷"成一个值（重点）
# ============================================================
# 大白话：reduce = "卷起来"。把列表从头到尾两两合并，
#         第一次拿前两个算，结果再和第三个算……最后只剩一个值。
# 用法：reduce(函数, 序列[, 初始值])
#       函数必须接收两个参数，返回一个值（这个值会继续参与下一次合并）
# 【补充】合并函数为什么必须接收"两个"参数？
#   reduce 每次调用合并函数时，都恰好传两个值进去（这就是"两两合并"）：
#     没写初始值：第一次 = (第1个元素, 第2个元素)，之后 = (上次结果, 下一个元素)
#     写了初始值：第一次 = (初始值, 第1个元素)，之后同上
#   所以形参只写一个（如 lambda x: x）会报错 TypeError：传了 2 个值接不住
#   （变量名随意起，但第 1 个变量 = 当前累积结果，第 2 个变量 = 下一个元素）
#   特例：序列只有 1 个元素且没写初始值 → 不调用合并函数，直接返回这个元素
#        空序列且没写初始值 → 报错（见下方陷阱）

import functools

# 例子 1：列表求和
nums = [1, 2, 3, 4, 5]
total = functools.reduce(lambda a, b: a + b, nums)
print(total)            # 15
# 【补充】它到底怎么算的？展开过程：
#   ((((1+2)+3)+4)+5)
#   = ((3+3)+4)+5
#   = (6+4)+5
#   = 10+5
#   = 15
#   第一次：a=1, b=2 → 3；第二次：a=3, b=3 → 6；
#   第三次：a=6, b=4 → 10；第四次：a=10, b=5 → 15

# 例子 2：连乘（算阶乘）
# 【怎么读】reduce 括号里按顺序：第 1 个 = 合并函数（决定两两怎么合并）；
#   第 2 个 = 要卷起来的序列；第 3 个（可选）= 初始值
#   这一行：lambda a, b: a * b = 两两相乘；range(1, 6) = [1, 2, 3, 4, 5]
fact = functools.reduce(lambda a, b: a * b, range(1, 6))
print(fact)             # 120     # 1*2*3*4*5

# 【补充】初始值（第三个参数）有什么用？
#   ① 空列表不报错：有初始值时，空列表直接返回初始值
#   ② 给第一次合并"打底"
print(functools.reduce(lambda a, b: a + b, [], 0))     # 0  （空列表也不报错）
print(functools.reduce(lambda a, b: a + b, [1, 2, 3], 100))  # 106  = 100+1+2+3
# 有初始值时：先拿 初始值和第一个元素 合并，再继续往后
# 没写初始值且列表为空 → 报错 TypeError: reduce() of empty sequence with no initial value
# 所以：处理"可能为空的列表"时，记得给初始值

# 【补充】reduce 也能干别的：找最大值
def bigger(a, b):
    return a if a > b else b
print(functools.reduce(bigger, [3, 8, 1, 6, 4]))   # 8
# 两两比较，把大的继续往下传 → 最后剩下最大那个
# 注意：这种"两两合并"的思想，后面学算法（归并、分治）还会遇到


# ============================================================
# 四、functools.partial：提前固定参数，造"专用函数"（重点）
# ============================================================
# 大白话：partial = "预填表单"。把一个函数的某些参数先填好，
#         得到一个新函数，之后调用只要填剩下的参数。
# 类比：点奶茶。partial 帮你提前选好"珍珠、三分糖、去冰"，
#       之后每次只需要说"要什么茶底"。
# 用法：functools.partial(原函数, 要固定的参数...)

# 例子 1：固定 pow 的指数，造一个"平方"函数
square = functools.partial(pow, exp=2)   # 固定指数为 2（用关键字固定第二个参数）
print(square(3))        # 9      # 等价于 pow(3, 2)
print(square(10))       # 100    # 等价于 pow(10, 2)

# 【补充】用 partial 固定参数，要不要记住参数名？
#   两种固定方式：
#     ① 按位置固定（不用记名字）：partial(pow, 2) —— 固定"第 1 个"参数，只能从左往右
#     ② 按关键字固定（要记名字）：partial(pow, exp=2) —— 固定"名叫 exp 的"参数
#   什么时候必须记名字？想固定"第 2 个及以后"的位置参数时：
#     按位置只能从左边开始、跳不过去，只能用关键字名来锁定
#   记不住名字怎么办？help(pow) 看签名 → pow(base, exp, mod=None)，名字一眼可见
#     自己写的函数：直接看 def 那行的参数名
#   小结：固定最左边第 1 个参数 → 不用记名字；固定后面的参数 → 必须知道参数名

# 【补充】只想固定"底数"怎么办？按位置固定第一个参数：
pow2 = functools.partial(pow, 2)   # 固定底数为 2 → 得到"2 的 n 次方"函数
print(pow2(3))          # 8      # 等价于 pow(2, 3)
# 关键点：partial 按位置固定时只能从左边开始；
#         想固定"第二个及以后"的位置参数，要用关键字名来固定
#         （pow 的第二个参数名是 exp，所以写 exp=2）

# 例子 2：固定 int 的进制，造一个"二进制转十进制"函数
bin2int = functools.partial(int, base=2)   # 固定关键字参数 base=2
print(bin2int("1010"))  # 10
print(bin2int("1111"))  # 15

# 例子 3：固定问候语的称呼
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

morning_greet = functools.partial(greet, greeting="早上好")
print(morning_greet("示其"))    # 早上好，示其
print(morning_greet("小明"))    # 早上好，小明

# 【补充】固定参数时要注意位置：
#   functools.partial(pow, 2) 是从左往右固定"前几个位置参数"
#   想固定后面的参数，要用关键字：partial(int, base=2)
#   （int 的第一个参数 x 不固定，只固定 base）

# 【补充】partial 的应用场景：
#   ① 同一函数被多次调用、每次都传相同参数 → 固定成专用函数
#   ② 传给回调函数/排序 key 时，需要"少一个参数的函数"
#      （后面做项目、写 GUI 回调时会大量用到）


# ============================================================
# 五、functools.lru_cache：记住算过的结果（缓存）（重点）
# ============================================================
# 大白话：lru_cache = "小本本"。函数每算出一个结果就记在小本本上，
#         下次遇到一模一样的参数，直接抄答案，不再重算。
# lru = Least Recently Used（最近最少使用）：小本本记满时，把最久没用的那条擦掉。
# 用法：在函数定义上面加 @functools.lru_cache(maxsize=128)
#       maxsize=128 表示最多记 128 条；maxsize=None 表示不限量

# 例子：斐波那契数列（经典慢例子）
# 斐波那契：fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# 不加缓存算 fib(35) 要好几秒（重复算了几百万次）
# 加了缓存，每个 n 只算一次，瞬间出结果：
# 【补充】开头的 @ 是干嘛的？（Day 19 学的装饰器语法糖）
#   @functools.lru_cache(maxsize=None) 等价于：
#     fib_fast = functools.lru_cache(maxsize=None)(fib_fast)
#   步骤拆开看：
#     ① functools.lru_cache(maxsize=None) 先调用 lru_cache（带参数 maxsize=None），得到一个"装饰器"
#     ② @ 把装饰器套在 fib_fast 上 = 加工出"带小本本记忆的新函数"，替换掉原来的 fib_fast
#   和 Day 19 的 @my_decorator 一样都是"给函数穿外套"；
#   区别只是 lru_cache 要先接收 maxsize 参数（None = 小本本不限量），所以多写一对括号
@functools.lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(50))     # 12586269025   （秒出）
# 对比：fib(35) 不用缓存就慢得明显，fib_fast(50) 却瞬间完成

# 【补充】为什么这么快？
#   不加缓存：fib(40) 要调 3 亿多次；fib(5) 内部 fib(2) 被算了好几次
#   加缓存：fib_fast(40) 每个 n 只真正算一次，其余全部"抄小本本"
#   第一次调用 fib_fast(50) 时已经把 0~49 全部算好记下了

# 【补充】怎么查看缓存情况？
print(fib_fast.cache_info())
# 输出类似：CacheInfo(hits=48, misses=51, maxsize=None, currsize=51)
#   hits    = 命中次数（抄小本本的次数）
#   misses  = 没命中、真正计算的次数
#   maxsize = 上限（None = 不限）
#   currsize = 当前记了多少条

# 【补充】两个大坑：
#   坑 1：lru_cache 装饰的函数，参数必须"可哈希"（能当字典键的）：
#         数字、字符串、元组 ✅；列表、字典 ❌（会报 TypeError: unhashable type）
#   坑 2：有"副作用"的函数别缓存！
#         比如函数里 print、改外部变量、读文件/时间——缓存后只执行一次，
#         后面的调用不再执行函数体，副作用也就没了（结果还是旧答案）
#   清理缓存：fib_fast.cache_clear() 清空小本本


# ============================================================
# 六、functools.cmp_to_key：把"比较函数"变成排序 key（重点）
# ============================================================
# 背景：sorted 的 key 只能给每个元素算"一个值"，按这个值排。
#       但有些排序规则"看两个元素的关系"，比如按字符串长度排、
#       按数字的个位数排——光看一个元素算不出。
# 旧式写法：写一个比较函数 cmp(a, b)，返回：
#       负数 → a 排在 b 前面；0 → 一样大；正数 → a 排在 b 后面
# functools.cmp_to_key(cmp函数) 把这个比较函数转成 sorted 能用的 key。
# 【补充】"转成 sorted 能用的 key"是什么意思？
#   sorted 的 key 只认"单参数函数"：key=lambda x: ... 给每个元素算一个值，按值排
#   而比较函数 cmp(a, b) 要两个参数 → 直接放 key= 位置会报错（少一个参数）
#   cmp_to_key 干的事：把你的 cmp 包装成"单参数、能比大小的特殊对象"，
#     排序时每两个包装对象比大小 → 自动调用你的 cmp(a, b) 来判谁大谁小
#   类比：cmp 是"裁判"（两两判大小）；sorted 只认"每人的号码牌"（key）；
#     cmp_to_key = 把裁判包装成魔法号码牌，贴给每个元素，排序时自动请裁判
#   对比：
#     sorted(words, key=len)                       # ✅ 单参数函数直接用
#     sorted(words, key=by_length)                 # ❌ by_length 要两个参数，报错
#     sorted(words, key=functools.cmp_to_key(by_length))  # ✅ 包装后就能用

# 例子 1：按字符串长度排序（短的在前）
def by_length(a, b):
    return len(a) - len(b)     # 长度差：负数=短的在前面

words = ["python", "java", "c", "go", "rust"]
sorted_words = sorted(words, key=functools.cmp_to_key(by_length))
print(sorted_words)     # ['c', 'go', 'java', 'rust', 'python']

# 例子 2：按"个位数"排序
def by_unit(a, b):
    return (a % 10) - (b % 10)   # 个位数小的在前

nums2 = [23, 41, 12, 35, 8]
sorted_nums = sorted(nums2, key=functools.cmp_to_key(by_unit))
print(sorted_nums)      # [41, 12, 23, 35, 8]
# 个位数分别是：1, 2, 3, 5, 8 → 升序

# 【补充】什么样的函数"既能用 lambda 写、也能用 def 写"，什么样"只能用 def 写"？
#   lambda 的规矩：只能写"一个表达式"，不能写多条语句（if / for / 赋值都不行）
#   注意：lambda 也可以有两个参数（lambda a, b: ...），限制只在"函数体只能是一个表达式"
#
#  ① 既能 lambda 也能 def：逻辑只有一个表达式 → 两种写法完全等价
#     例：按长度升序的比较函数（函数体就一句 return len(a) - len(b)）
def by_len_def(a, b):                               # def 写法
    return len(a) - len(b)

by_len_lambda = lambda a, b: len(a) - len(b)        # lambda 写法，功能一模一样

words3 = ["python", "c", "go"]
print(sorted(words3, key=functools.cmp_to_key(by_len_def)))     # ['c', 'go', 'python']
print(sorted(words3, key=functools.cmp_to_key(by_len_lambda)))  # ['c', 'go', 'python'] 结果一样
#
#  ② 只能用 def 写：逻辑要"多条语句"（if 分支等）→ lambda 单表达式写不了
#     例：先比长度，长度相同再比字典序（需要 if 分支）
def by_len_then_alpha(a, b):
    if len(a) != len(b):        # 长度不同：短的在前
        return len(a) - len(b)
    if a < b:                   # 长度相同：字典序小的在前
        return -1
    if a > b:
        return 1
    return 0

words4 = ["bb", "a", "aa", "b"]
print(sorted(words4, key=functools.cmp_to_key(by_len_then_alpha)))
# ['a', 'b', 'aa', 'bb']：先按长度 1、1、2、2，长度相同的 a<b、aa<bb

# 【补充】为什么不能用普通 key 做"按个位数排"？
#   key=lambda x: x % 10 其实可以！个位数就是一个"值"
#   cmp_to_key 的真正优势是"需要同时看两个元素"的规则，
#   比如：按 a+b 和 b+a 的字典序排（字符串拼接比较大小），
#   key 算不出（要两两比较），只能写 cmp 函数。
#   一句话：能写 key 就写 key（更快）；规则需要"两两比"才用 cmp_to_key。

# 【补充】比较函数返回值的约定（务必记住）：
#   返回 负数：a < b（a 排前面）
#   返回 0：a == b
#   返回 正数：a > b（a 排后面）
#   常见写法：return a - b（数字比大小）；return len(a) - len(b)（比长度）
# 【补充】为什么"返回负数 = a 排前面"？（把这一点想通就全懂了）
#   sorted 把返回值当成"a - b 的符号"来用，数学上：
#     a - b < 0  ⟺  a < b  ⟺  升序时 a 该排在 b 前面
#   所以 return a - b 天然就是"升序比较器"：
#     例：比较 (3, 5) → 3-5 = -2 < 0 → 3 在前 → 升序 ✓
#   想降序：把减法反过来 return b - a（或直接用 reverse=True，见下一条补充）

# 【补充】排序方向：想倒序，两种办法
#   ① sorted(..., reverse=True)
#   ② 比较函数里把减法反过来：return len(b) - len(a)
#   推荐 ①，语义更清楚。


# ============================================================
# 七、例题精讲（看懂了再去做练习）
# ============================================================

# ------------------------------------------------------------
# 例题 1：用 reduce 求列表中所有数的乘积
# 思路：reduce(lambda a, b: a * b, 列表)，空列表给初始值 1
# ------------------------------------------------------------
prod = functools.reduce(lambda a, b: a * b, [2, 3, 4], 1)
print(prod)             # 24     # (((1*2)*3)*4)

# ------------------------------------------------------------
# 例题 2：用 partial 造一个"固定底数 3 的幂"函数
# 思路：functools.partial(pow, 3)
# ------------------------------------------------------------
pow3 = functools.partial(pow, 3)
print(pow3(2))          # 9      # 3**2
print(pow3(4))          # 81     # 3**4

# ------------------------------------------------------------
# 例题 3：用 lru_cache 优化"爬楼梯"问题
# 题目：上 n 级台阶，每次可以走 1 级或 2 级，共有多少种走法？
# 思路：f(n) = f(n-1) + f(n-2)，f(1)=1, f(2)=2（本质和斐波那契一样）
# 【补充】这个思路怎么来的？（数学递推）
#   核心：看"最后一步"怎么走，分类讨论：
#     最后一步走 1 级 → 之前已在第 n-1 级 → 走法数 f(n-1)
#     最后一步走 2 级 → 之前已在第 n-2 级 → 走法数 f(n-2)
#   两种可能互斥，加起来：f(n) = f(n-1) + f(n-2)（递推公式）
#   边界：f(1)=1（只能走1级）、f(2)=2（1+1 或直接2）
#   往下一项项推：f(3)=3, f(4)=5, f(5)=8, f(6)=13, f(7)=21, f(8)=34, f(9)=55, f(10)=89
#   和斐波那契 F(1)=1,F(2)=1 的关系：爬楼梯序列 = 斐波那契右移一位（f(n) = F(n+1)）
#   代码 = 递推公式直译：n=1/n=2 是递归出口，n>2 拆成两个小问题再相加
# ------------------------------------------------------------
# 【补充】拿小数字 n=5 走一遍缓存流程（小本本 = lru_cache）
#   调用 climb(5)（Python 先算左支 climb(n-1)，再算右支 climb(n-2)）：
#     ① climb(5) 没记录 → 真算，需要 climb(4)+climb(3)
#     ② climb(4) 没记录 → 真算，需要 climb(3)+climb(2)
#     ③ climb(3) 没记录 → 真算，需要 climb(2)+climb(1)
#     ④ climb(2) 没记录 → 真算 = 2（边界），记下 climb(2)=2
#     ⑤ climb(1) 没记录 → 真算 = 1（边界），记下 climb(1)=1
#     ⑥ climb(3) = 2+1 = 3，记下 climb(3)=3
#     ⑦ 回到 climb(4)：climb(2) 小本本有 → 直接抄 2 → 3+2=5，记下 climb(4)=5
#     ⑧ 回到 climb(5)：climb(3) 小本本有 → 直接抄 3 → 5+3=8，记下 climb(5)=8
#   最终小本本：{1:1, 2:2, 3:3, 4:5, 5:8}
#   实测 climb.cache_info()：hits=2（抄了 climb(2)、climb(3)），misses=5（每个 n 真算一次）
#   对比不用缓存：climb(5) 要真正执行函数体 9 次（climb(2) 算了 3 遍、climb(3) 算了 2 遍）
#   n 越大差距越夸张：climb(30) 不缓存要算几百万次，缓存后每个 n 只算一次
@functools.lru_cache(maxsize=None)
def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb(n - 1) + climb(n - 2)

print(climb(10))        # 89
# 不用缓存算 climb(35) 就明显卡顿，加了缓存 climb(100) 也瞬间算完

# ------------------------------------------------------------
# 例题 4：用 cmp_to_key 把数字按"字符串拼接后从大到小"排序
# 题目：给 [3, 30, 34, 5, 9]，排成能拼出最大数字的顺序
# 思路：比较 a 和 b 时，看 str(a)+str(b) 和 str(b)+str(a) 谁大
# ------------------------------------------------------------
def bigger_join(a, b):
    # 想让"拼接后更大的"排前面：比较 a+b 与 b+a，大的在前 → 返回负的
    return int(str(b) + str(a)) - int(str(a) + str(b))

arr = [3, 30, 34, 5, 9]
result = sorted(arr, key=functools.cmp_to_key(bigger_join))
print(result)           # [9, 5, 34, 3, 30]
print("".join(map(str, result)))   # 9534330   ← 能拼出的最大数字
# 【补充】为什么 3 排在 30 前面？
#   "330" > "303"，所以 3 应该排在 30 前面
#   key 只算单个数算不出这种"拼接后比大小"，必须两两比较 → cmp_to_key 出场

# ------------------------------------------------------------
# 例题 5：keyword-only 参数做"必填校验"
# 题目：写 create_user，用户名按位置传，年龄必须用关键字传且必须提供
# ------------------------------------------------------------
def create_user(name, *, age):
    # age 在 * 后面：必须写 age=xx 才能调用，漏了直接报错
    return {"name": name, "age": age}

print(create_user("示其", age=18))
# 输出：{'name': '示其', 'age': 18}
# create_user("示其")  ← 会报错 TypeError: create_user() missing 1 required keyword-only argument: 'age'
# 好处：调用者一眼看出"哦，age 是必填的"，漏传时 Python 主动提醒，不会默默用错值


# ============================================================
# 八、常见陷阱
# ============================================================
# 陷阱 1：reduce 没给初始值 + 空列表 → TypeError 报错
#   解决：可能为空的列表，给第三个参数初始值
#
# 陷阱 2：partial 固定位置参数只能从左边开始
#   想固定后面的参数 → 用关键字：partial(int, base=2)
#
# 陷阱 3：lru_cache 装饰"参数含列表/字典"的函数 → unhashable type 报错
#   解决：把参数改成元组/字符串，或不用缓存
#
# 陷阱 4：lru_cache 装饰"有副作用"的函数（print、读文件、取时间）
#   缓存后函数体只真正执行一次，副作用和"新答案"都会消失
#
# 陷阱 5：cmp_to_key 的比较函数返回约定记反
#   返回 负数 = a 排前面（不是"正数排前面"！）
#
# 陷阱 6：keyword-only 参数无默认值又没传 → 报错
#   这是特性不是 bug：它逼你在调用时写清楚参数名


# ============================================================
# 九、今天总结（一图流）
# ============================================================
# keyword-only：def f(a, *, b) —— b 只能关键字传（防传错、更清晰）
# reduce：把列表"卷"成一个值，两两合并（求和、连乘、找最大）
# partial：预填参数，造专用函数（固定底数、固定进制、固定称呼）
# lru_cache：小本本记答案，重复参数直接抄（斐波那契秒算）
# cmp_to_key：旧式比较函数 → sorted 的 key（需要两两比较的规则）
#
# 明天 Day 21：异常进阶（raise、assert、自定义异常、异常链）
