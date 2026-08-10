# Day 15 · 代码测试专用 (2026.8.10)
# 在这里随便写、随便试，不影响正式练习。

# 示例：嵌套数据
students = [
    {"name": "张三", "score": 95, "city": "重庆"},
    {"name": "李四", "score": 82, "city": "北京"},
]

# 示例：取第一层
print(students[0])
print(students[0]["name"])

# 示例：按分数排序
print(sorted(students, key=lambda s: s["score"], reverse=True))
