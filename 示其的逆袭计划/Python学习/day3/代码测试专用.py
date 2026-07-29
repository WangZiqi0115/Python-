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
text = "apple banana apple orange banana apple"
print(type(text.split()))
