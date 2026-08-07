"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 12 准备就绪！")
# student = {}
# def add_contact(contacts, name, phone, city):
#     # 请在此处编写代码
#     contacts[name] = {"phone":phone,"city":city}
#     return contacts
# add_contact(student,"张三",123456,"重庆")
# add_contact(student,"李四",123456,"重庆")
  
# def list_contacts(contacts):
#     count = 0  
#     for name,info in contacts.items():
#         print(f"{name} {info["phone"]} {info["city"]}")
#         count += 1
#     print(f"联系人数量为{count}")
# list_contacts(student)
# def find_contact(contacts, name):
#     data =contacts.get(name,None)
#     print((data["phone"],data["city"]))
# find_contact(student,"张三")
def add_contact(contacts, name, phone, city):
    # 请在此处编写代码
    contacts[name] = {"phone":phone,"city":city}
    return contacts


# ============================================================
# 任务 2 · 查看所有联系人（10 分）
# 打印所有联系人，格式：
#   张三  13800138000  重庆
# 返回联系人数量
# ============================================================
def list_contacts(contacts):
    count = 0
    for name,info in contacts.items():
        print(f"{name} {info["phone"]} {info["city"]}")
        count += 1
    return(f"联系人数量为{count}")


# ============================================================
# 任务 3 · 按姓名查找（10 分）
# 找到 → 返回 (phone, city)
# 找不到 → 返回 None
# ============================================================
def find_contact(contacts, name):
    # 请在此处编写代码
    data =contacts.get(name)
    if data :
        return((data["phone"],data["city"]))
    else:
        return None
student = {}
add_contact(student,"张三","123456","重庆")
add_contact(student,"李四","456789","成都")

# print(find_contact(student,"张三"))
# delete = student.pop("王五",None)
# if delete:
#         print (True)
# else:
#         print (False)
# print(student)
# dic = {}
# with open("test.txt","r",encoding="utf-8") as f:
#     lines = [line.strip().split(",") for line in f]
#     for i in range(len(lines)):
#         dic[lines[i][0]] = {"phone":lines[i][1],"city":lines[i][2]}
#     print(dic)
dct = {'张三': {'phone': '123456', 'city': '重庆'}, '李四': {'phone': '542556', 'city': '重庆'}}
for name,info in dct:
    print(name,info)
    
    
