# # 情况1：直接赋初始值 None，后面再改
# d = {}
# d["score"] = None      # 先占个位
# print(d)               # {"score": None}
# # 后面再来赋值
# d["score"] = 95
# print(d)               # {"score": 95}

# # 情况2：别想太多，用的时候直接加
# d = {}
# if some_condition:
#     d["score"] = 95    # 需要的时候再赋值

# # 如果你有多个键需要先占位
# keys = ["math", "english", "python"]
# d = {k: None for k in keys}
# print(d)               # {"math": None, "english": None, "python": None}
# # 后面再逐个赋值
# d["math"] = 90
# d["python"] = 95
# text = "apple banana apple orange banana apple"
# print(type(text.split()))
scores = {"张三": 95, "李四": 87, "王五": 92, "赵六": 78}
    
total = 0
count = 0
    # 请在此处编写代码：遍历并打印
# for name,score in scores.items():
#     print(f"姓名：{name}，分数：{score}")
#     total = score + total
#     count += 1
# print(total,count)
text = "Hello world hello Python world hello"
freq = {}
    # 请在此处编写代码
for word in text.split():
    word = word.lower()
    freq[word] = freq.get(word,0) + 1
print(freq)
