# python_base.py 对比分析

> 来源：[xianhu/LearnPython/python_base.py](https://github.com/xianhu/LearnPython/blob/master/python_base.py)
> 分析时间：2026.8.8（Day 13 完成后）
> 用途：检查过去两周所学内容与这份经典 Python 基础速查的差距，指导后续 50 天计划。

---

## 一、总体结论

`python_base.py` 是一份 1336 行的语法大全式速查，覆盖面比日常项目更广，其中包含不少 Python 2 时代遗留内容。示其过去两周（Day 1-13）走的是应用导向路线，四大容器、字符串、函数、文件、异常、模块等核心内容已经覆盖，并不落后。

真正的差距集中在：

1. 数字类型与位运算
2. 高级解包
3. 函数进阶（闭包 / 装饰器 / keyword-only / reduce）
4. 迭代器协议
5. 异常进阶（raise / assert / 自定义异常）
6. 字符编码与 bytes
7. 文件进阶（seek / tell / 二进制）
8. 类与面向对象（最大的一块空白）

---

## 二、已经覆盖的内容（基本无出入）

| 主题 | 说明 |
|------|------|
| 四大容器 | 增删改查、切片、推导式、排序、遍历、嵌套、复制与引用模型 |
| 字符串 | 大小写、查找、判断、split/join、strip、三种格式化方式 |
| 集合 | 并集/交集/差集/对称差集、子集判断、frozenset、哈希原理 |
| 字典 | get/setdefault/fromkeys/defaultdict、嵌套、推导式 |
| 函数 | 位置/关键字/默认参数、return、lambda、*args/**kwargs、map/filter |
| 生成器 | 生成器表达式、yield、一次性消费 |
| 文件与异常 | with、r/w/a、read/readline/readlines、try/except/else/finally |
| 模块与包 | import/from/as、__name__、__init__.py、搜索路径 |
| 常用内置函数 | len/sum/max/min/sorted/enumerate/zip/range/type/isinstance/bool/input/open |

---

## 三、文件里有、尚未系统学的内容（按优先级排序）

### 高优先级：近期就应该补

| 主题 | 具体内容 |
|------|---------|
| 高级解包 | `a, *b, c = [1, 2, 3, 4]`、嵌套解包、调用解包 `func(*args)` / `func(**kwargs)`、`zip(*data)` |
| 数字与位运算 | 进制 `0x/0o/0b`、`bin/oct/hex`、`int("1001", 2)`、`bit_length`、位运算 `& \| ^ << >> ~` |
| 迭代器协议 | `iter()` / `next()`、for 循环底层、StopIteration、自定义可迭代对象 |
| 异常进阶 | `raise` 主动抛错、`assert`、自定义异常类、异常链、else/finally 深入 |

### 中优先级：函数深水区

| 主题 | 具体内容 |
|------|---------|
| 闭包与作用域 | 嵌套函数、LEGB 查找顺序、nonlocal、闭包工厂函数 |
| 装饰器 | 装饰器原理、@ 语法、functools.wraps、计时/日志装饰器 |
| functools | reduce、partial、lru_cache、cmp_to_key |
| keyword-only 参数 | `def f(a, *, b)` 中 * 后面的参数必须用关键字传 |

### 中优先级：标准库与数据

| 主题 | 具体内容 |
|------|---------|
| 文件进阶 | seek/tell/flush/writelines、二进制 rb/wb、os.path/pathlib |
| JSON / CSV | json 模块、csv 模块、数据交换与清洗 |
| datetime / time | 日期时间格式化、strftime/strptime、timedelta、时间戳 |
| random | 随机数、洗牌、抽样、蒙特卡洛模拟 |
| collections | Counter、defaultdict、namedtuple、deque |
| itertools | chain、product、permutations、combinations、groupby |
| 正则进阶 | re.sub/re.split/finditer、命名分组、非贪婪、flags、compile |

### 需要系统学习：类与 OOP

| 主题 | 具体内容 |
|------|---------|
| OOP 入门 | class/self、__init__、实例变量/类变量、方法 |
| 继承 | 单继承、super、方法重写、多态、isinstance/issubclass |
| OOP 进阶 | 类方法/静态方法、property、私有属性、__slots__ |
| 魔法方法 | __str__/__repr__/__len__/__getitem__/__setitem__/__iter__/__next__/__call__/__eq__ |

> 昨天（Day 13）的 class 入门示例只开了个头，OOP 是后续 50 天计划中的系统专题。

### 了解即可

- 字符编码原理：ASCII / Unicode / UTF-8 / GBK、str vs bytes、encode/decode
- 模块进阶：sys.argv / sys.path、__all__、__doc__ / __file__、相对导入
- 冷门内置函数：eval/exec（注意安全）、getattr/setattr/hasattr、repr、vars、divmod、ord/chr
- 调试与规范：logging、pdb、PEP8、类型注解、docstring

---

## 四、文件里过时或不能直接照抄的内容

| 内容 | 原因 |
|------|------|
| raw_input、long、cmp、execfile、unichr、reload | Python 2 遗留，Python 3 已删除或改名 |
| `I.next()` | Python 3 用 `next(I)` |
| `def selfless(message)` 类里不写 self | Python 3 中这样调用会出错 |
| `c = t – s`（全角减号） | 语法错误，应写 `t - s` |
| `A = 1 if X else 2` 等示例 | X 未定义，不能直接运行，只能看写法 |
| 函数属性 `func.count = 1` | 偏冷门，实际项目很少用 |

---

## 五、反向差异：文件里没有、但你已经在学的

| 内容 | 说明 |
|------|------|
| 正则表达式 | Day 13 已入门，文件完全没有正则章节 |
| f-string | 你已经在用，文件只讲了 % 和 .format |
| 项目实战 | 通讯录 v1 已完成，后续还有 v2 |
| 爬虫方向 | 文件没有，已排进 50 天计划 |
| NumPy / Pandas | 文件没有，按新计划往后放 |

---

## 六、对应计划调整

- 原 30 天计划延长为 **50 天**，每天一个主题，不图快
- 数模三件套从 Day 14-20 后移到 **Day 48-50**
- Day 14-22 补齐 python_base 中的语法深水区
- Day 15 插入小专题：嵌套数据结构实战（容器组合场景，爬虫/数模/刷题常用）
- Day 23-31 补齐标准库与数据工具
- Day 32-39 系统学习 OOP 并做两个综合项目
- Day 40-47 爬虫 + 算法思维
- Day 48-50 数模入门 + 总结

详细安排见 [Python学习计划.md](Python学习计划.md)。
