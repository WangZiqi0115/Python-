"""给定学生成绩字典：
```python
students = {"张三": 90, "李四": 75, "王五": 88, "赵六": 60}
```
请写一个函数 `pass_list(d)`：返回**成绩 ≥ 80** 的学生**名字列表**（保持 dict 里的顺序即可）。提示：用 `d.items()` 遍历 + 列表推导式。**先自己写，别急着看答案。**"""
def pass_list(d):
    return[name for name,score in d.items() if d[name] >= 80]
students = {"张三": 90, "李四": 75, "王五": 88, "赵六": 60}
print(pass_list(students))