"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 11 准备就绪！")
# scores = {"张三": 95, "李四": 82, "王五": 90, "赵六": 76}
# wang_score = scores.get("王五",0)   # 请修改：get 取王五，默认 0
# avg = sum(num for num in scores.values())  / len(scores)        # 请修改：平均分保留1位
# top_student = max(scores.items(),key = lambda x:x[1])[0]
# print(top_student)
# with open("text.txt","w",encoding="utf-8") as f:
#     f.write("张三,95\n李四,87\n王五,92\n")
# # 
# with open("text.txt","r",encoding="utf-8") as f: 
    
#     scores = [score.strip().split(",")[1] for score in f]
#     print(scores)
students = [
        {"name": "张三", "score": 95},
        {"name": "李四", "score": 82},
        {"name": "王五", "score": 90},
        {"name": "赵六", "score": 76},
    ]
scores = [score["score"] for score in students]       # 请修改：所有成绩列表
top_names = [name["name"] for name in students if name["score"] >= 90]    # 请修改：>= 90 的姓名
ranked = [s["name"] for s in sorted(students,key=lambda x:x["score"],reverse=True)  ]     # 请修改：按成绩降序的姓名列表
print(ranked)
