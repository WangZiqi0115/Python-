# Python 学习计划（50 天）

示其的 Python 学习路线 —— 从入门到实战，目标跨考浙大计算机学硕。

调整说明（2026.8.8）：

- 原 30 天计划延长为 **50 天**，每天都有内容，不设休息日
- 不图快，每天只深入一个主题，配知识点、练习、代码测试专用三样文件
- 数模三件套从 Day 14-20 **后移到 Day 48-50**
- Day 14 起补齐 python_base 对比中发现的语法深水区

---

## 第一阶段 · 已完成的语法基础（Days 1-13）

| 天 | 日期 | 内容 | 状态 |
|----|------|------|------|
| 1 | 7.27 | List 全家桶 | ✅ 已完成 |
| 2 | 7.28 | Tuple + 可变不可变 | ✅ 已完成 |
| 3 | 7.29 | Dict 字典 | ✅ 已完成 |
| 4 | 7.30 | Set 集合 | ✅ 已完成 |
| 5 | 7.31 | 字符串方法（split / join / replace / strip...） | ✅ 已完成 |
| 6 | 8.1 | 四大容器综合串讲 + 阶段练习 | ✅ 已完成 |
| 7 | 8.2 | 函数专题：def、参数、返回值、作用域 | ✅ 已完成 |
| 8 | 8.3 | 文件 I/O + 异常处理 | ✅ 已完成 |
| 9 | 8.4 | 模块与包、常用内置函数 | ✅ 已完成 |
| 10 | 8.5 | 列表推导式 + 生成器 + lambda 进阶 | ✅ 已完成 |
| 11 | 8.6 | 综合练习 | ✅ 已完成 |
| 12 | 8.7 | 小项目：通讯录管理系统 | ✅ 已完成 |
| 13 | 8.8 | 正则表达式入门（re 模块） | ✅ 已完成 |

---

## 第二阶段 · 语法深水区与容器实战（Days 14-22）

| 天 | 日期 | 内容 | 深入要点 |
|----|------|------|---------|
| 14 | 8.9 | 数字类型与运算符深挖（✅ 已完成） | int/float/bool/complex、进制、hex/oct/bin、int(s, base)、bit_length、浮点误差、inf/nan；算术/比较/逻辑/成员/身份运算符、位运算 `& \| ^ << >> ~`、连续比较、优先级表 |
| 15 | 8.10 | 小专题：嵌套数据结构实战（✅ 已完成） | list 套 dict / dict 套 list、多层安全访问、按字段排序、defaultdict 分组、反转/合并字典、提取与扁平化、JSON 结构预览 |
| 16 | 8.11 | 高级解包（✅ 已完成） | `a, *b, c` 星号解包、嵌套解包、调用解包 `func(*args)` / `func(**kwargs)`、`zip(*data)` |
| 17 | 8.12 | 迭代器协议（✅ 已完成） | iter/next、for 循环底层、StopIteration、自定义可迭代对象、常见迭代器 |
| 18 | 8.13 | 闭包与作用域（✅ 已完成） | 嵌套函数、LEGB 查找顺序、nonlocal、闭包工厂、闭包陷阱 |
| 19 | 8.14 | 装饰器入门（✅ 已完成） | 装饰器原理、@ 语法、functools.wraps、计时/日志装饰器 |
| 20 | 8.15 | functools 与 keyword-only（✅ 已完成） | reduce、partial、lru_cache、cmp_to_key、* 后面的必关键字参数 |
| 21 | 8.16 | 异常进阶 | raise、assert、自定义异常、异常链、else/finally 深入 |
| 22 | 8.17 | 编码与 bytes | ASCII/Unicode/UTF-8/GBK、str vs bytes、encode/decode、乱码原理 |

---

## 第三阶段 · 标准库与数据处理（Days 23-31）

| 天 | 日期 | 内容 | 深入要点 |
|----|------|------|---------|
| 23 | 8.18 | 文件进阶与路径 | seek/tell/flush/writelines、二进制 rb/wb、os.path/pathlib、遍历目录 |
| 24 | 8.19 | JSON 数据交换 | json.dumps/loads、ensure_ascii=False、嵌套数据、与文件结合 |
| 25 | 8.20 | CSV 与数据清洗 | csv 模块读写、分隔符、清洗 pipeline、编码处理 |
| 26 | 8.21 | datetime / time | 日期时间对象、strftime/strptime、timedelta、时间戳、计时 |
| 27 | 8.22 | random 与模拟 | 随机数、洗牌、抽样、蒙特卡洛、随机密码 |
| 28 | 8.23 | collections | Counter、defaultdict、namedtuple、deque、词频统计 |
| 29 | 8.24 | itertools | count/cycle/repeat/chain/product/permutations/combinations/groupby |
| 30 | 8.25 | 正则进阶 | re.sub/split/finditer、命名分组、非贪婪、flags、compile |
| 31 | 8.26 | 正则综合实战 | 手机号/邮箱/身份证/URL/IP 提取、日志清洗 |

---

## 第四阶段 · OOP 与工程化（Days 32-39）

| 天 | 日期 | 内容 | 深入要点 |
|----|------|------|---------|
| 32 | 8.27 | OOP 入门 | class/self、__init__、实例变量/类变量、方法、__str__/__repr__ |
| 33 | 8.28 | 继承 | 单继承、super、方法重写、多态、isinstance/issubclass |
| 34 | 8.29 | OOP 进阶 | 类方法/静态方法、property、私有属性、__slots__ |
| 35 | 8.30 | 魔法方法 | __len__/__getitem__/__setitem__/__iter__/__next__/__call__/__eq__、__enter__/__exit__（with 上下文管理器） |
| 36 | 8.31 | 模块与包深入 | sys.argv/sys.path、__all__、__doc__/__file__、相对导入 |
| 37 | 9.1 | 调试与代码规范 | logging、pdb、断言、PEP8、类型注解、docstring |
| 38 | 9.2 | 项目：通讯录 v2 | 类 + JSON 持久化 + 正则校验 + 异常处理 |
| 39 | 9.3 | 项目：学生成绩系统 | 文件 + 统计 + 排序 + 报告输出 |

---

## 第五阶段 · 爬虫与算法思维（Days 40-47）

| 天 | 日期 | 内容 | 深入要点 |
|----|------|------|---------|
| 40 | 9.4 | 爬虫基础 | HTTP 概念、requests、get/post、headers、状态码 |
| 41 | 9.5 | 爬虫进阶 | BeautifulSoup、选择器、提取、保存 CSV/JSON、robots 与反爬 |
| 42 | 9.6 | 爬虫实战 | 抓取一个简单静态站点并清洗（本地 HTML 示例保底） |
| 43 | 9.7 | 算法基础 1 | 时间复杂度概念、双指针、滑动窗口 |
| 44 | 9.8 | 算法基础 2 | 哈希表与计数、两数之和、众数 |
| 45 | 9.9 | 算法基础 3 | 手写冒泡/选择/插入排序、二分查找 |
| 46 | 9.10 | 算法基础 4 | 递归三要素、排列组合、迷宫回溯入门 |
| 47 | 9.11 | 算法基础 5 | 栈与队列、括号匹配、单调栈概念 |

---

## 第六阶段 · 数模收尾（Days 48-50，数模后移到这里）

| 天 | 日期 | 内容 | 深入要点 |
|----|------|------|---------|
| 48 | 9.12 | NumPy 基础 | 数组创建、索引、运算、矩阵 |
| 49 | 9.13 | Pandas 基础 | Series/DataFrame、筛选、分组、聚合 |
| 50 | 9.14 | Matplotlib + 总结 | 可视化基础、一个完整数据小案例、50 天查漏补缺、Python 经典陷阱查漏 |

---

## 参考资源与借鉴仓库（2026.8.8 整理）

### 高分学习路线与练习来源

| 仓库 | 星标 | 借鉴点 |
|------|------|--------|
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 27.7 万 | 项目式学习，Day 38/39/42 项目的备选灵感来源 |
| [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 18.5 万 | 分阶段路线，50 天结束后可继续往下走 |
| [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 7 万 | 每天一课的练习节奏，补充题目来源 |
| [dabeaz-course/practical-python](https://github.com/dabeaz-course/practical-python) | 1.1 万 | 实战导向课程，练习风格值得参考 |
| [michaelliao/learn-python3](https://github.com/michaelliao/learn-python3) | 0.6 万 | 廖雪峰 Python 3 示例代码，中文查阅方便 |

### 查漏与工具

| 仓库 | 星标 | 借鉴点 |
|------|------|--------|
| [gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet) | 3.9 万 | 综合速查表，和 python_base 互补 |
| [satwikkansal/wtfpython](https://github.com/satwikkansal/wtfpython) | 3.7 万 | Python 反直觉陷阱，Day 50 查漏素材 |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 22.4 万 | Day 43-47 算法实现参考 |
| [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | 5 万 | Day 48-50 数模阶段参考 |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 31.3 万 | 日后查库目录，遇到需求先来这里找轮子 |

### LearnPython 仓库实例对照

| 计划中的天 | 对应实例 |
|-----------|---------|
| Day 19 装饰器 | python_decorator.py |
| Day 20 函数式工具 | python_functional.py |
| Day 25 CSV | python_csv.py |
| Day 26 时间处理 | python_datetime.py |
| Day 30-31 正则 | python_re.py |
| Day 35 魔法方法 | python_magic_methods.py |
| Day 40-42 爬虫 | python_requests.py / python_spider.py |
| Day 48 NumPy | python_numpy.py |
| Day 50 收尾彩蛋 | python_oneline.py |

> 元类、协程、多线程、Flask、SQLAlchemy、Redis、socket 等属于进阶方向，不进 50 天，留到大一下及以后。

---

## 长期目标

- 暑假到开学初：掌握 Python 基础到应用，能独立写题、做小项目
- 大一：主攻 C++，数据结构入门，数学建模竞赛启动
- 大二：数学建模竞赛 + 408 专业课启动
- 大三：408 复习 + 考研冲刺
- 目标院校：浙江大学 计算机学硕
