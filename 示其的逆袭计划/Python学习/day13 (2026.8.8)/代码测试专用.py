"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 13 准备就绪！")
# import re
# text = "我有3个苹果和12个橘子"
# result = re.findall(r"\d+",text)
# print(resu)
# import re
# log = "192.168.1.1 - - [08/Aug/2026] GET /index.html"
# ip = re.findall("\d+\.\d+\.\d+\.\d+",log).group()  # 请修改：提取 IP
# print (ip)
# s = "张三:95 李四:87 王五:92"
# import re
# data = re.findall(r"(\w+):(\d+)",s)
# print(sum(int(score[1]) for score in data)
# )
import re
text = "张三 13800138000 重庆"
    # 请在此处编写代码：提取姓名、电话、城市
data = re.search(r"(\w+) (\d{11}) (\w+)",text)
name = data.group(1)
phone = data.group(2)
city = data.group(3)
print(name)