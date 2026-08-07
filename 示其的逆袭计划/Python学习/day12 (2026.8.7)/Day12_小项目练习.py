"""
Day 12 · 小项目实战：通讯录管理系统 (2026.8.7)
=================================================
今天做一个完整项目，把前 11 天学的知识全部串起来。

项目需求：
1. 添加联系人（姓名、电话、城市）
2. 查看所有联系人
3. 按姓名查找联系人
4. 删除联系人
5. 保存到文件 / 从文件读取

先实现下面的函数，最后运行测试评分。
"""

# ============================================================
# 任务 1 · 添加联系人（10 分）
# 往 contacts 字典里添加联系人
# 结构：{"张三": {"phone": "138...", "city": "重庆"}}
# 返回修改后的字典
# ============================================================
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
        print(f"{name} {info['phone']} {info['city']}")
        count += 1
    return count


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


# ============================================================
# 任务 4 · 删除联系人（10 分）
# 删除成功 → 返回 True
# 联系人不存在 → 返回 False
# ============================================================
def delete_contact(contacts, name):
    # 请在此处编写代码
    delete = contacts.pop(name,None)
    if delete:
        return True
    else:
        return False


# ============================================================
# 任务 5 · 保存到文件（10 分）
# 每行格式：姓名,电话,城市
# ============================================================
def save_contacts(filename, contacts):
    # 请在此处编写代码
    with open(filename,"w",encoding="utf-8") as f:
        for name,info in contacts.items():    
            f.write(f"{name},{info['phone']},{info['city']}\n")


# ============================================================
# 任务 6 · 从文件读取（10 分）
# 文件不存在 → 返回空字典
# ============================================================
def load_contacts(filename):
    # 请在此处编写代码
    try:
        dic = {}
        with open(filename,"r",encoding="utf-8") as f:
            lines = [line.strip().split(",") for line in f]
            for i in range(len(lines)):
                dic[lines[i][0]] = {"phone":lines[i][1],"city":lines[i][2]}
        return dic
    except FileNotFoundError:
        return{}
    
            


# ============================================================
# 任务 7 · 综合：完整流程（10 分）
# 模拟一次使用流程：
#   1. 添加张三
#   2. 添加李四
#   3. 查找李四
#   4. 删除张三
#   5. 保存到文件
#   6. 从文件重新读取
#   返回 (查找结果, 删除结果, 重新读取的字典)
# ============================================================
def full_flow(filename):
    contacts = {}
    # 请在此处编写代码
    add_contact(contacts,"张三","13800138000","重庆")
    add_contact(contacts,"李四","13900139000","北京")
    find_result = find_contact(contacts,"李四")
    delete_result = delete_contact(contacts,"张三")
    save_contacts(filename,contacts)
    loaded = load_contacts(filename)
    
    return find_result, delete_result, loaded


# ============================================================
# 任务 8 · 主菜单（10 分）
# 实现菜单循环：
#   1 添加  2 查看  3 查找  4 删除  5 退出
# 输入 5 退出循环，返回操作次数
# ============================================================
def main_menu(contacts):
    actions = 0
    while True:
        print("\n1. 添加  2. 查看  3. 查找  4. 删除  5. 退出")
        choice = input("请选择：")
        
        if choice == "5":
            break
        elif choice == "4":
            actions += 1
            delete_contact(contacts,input("请输入删除的名字"))
        elif choice == "3":
            actions += 1
            find_contact(contacts,input("请输入要查找的名字"))
        elif choice == "2":
            actions += 1
            list_contacts(contacts)
        elif choice == "1":
            actions += 1
            add_contact(contacts,input("请输入要添加的姓名"),input("请输入要添加的电话"),input("请输入要添加的城市"))
        # 请在此处编写代码：处理 1-4 选项，每成功操作一次 actions += 1
    
    return actions


# ============================================================
# 以下为测试代码，请勿修改
# ============================================================
if __name__ == "__main__":
    import os
    score = 0
    print("=" * 40)

    # 任务 1
    try:
        contacts = {}
        add_contact(contacts, "张三", "13800138000", "重庆")
        assert contacts == {"张三": {"phone": "13800138000", "city": "重庆"}}, f"添加错误: {contacts}"
        score += 10
        print("[PASS] 任务 1")
    except Exception as e:
        print(f"[FAIL] 任务 1: {e}")

    # 任务 2
    try:
        contacts = {"张三": {"phone": "13800138000", "city": "重庆"}, "李四": {"phone": "13900139000", "city": "北京"}}
        n = list_contacts(contacts)
        assert n == 2, f"数量应为 2，得到 {n}"
        score += 10
        print("[PASS] 任务 2")
    except Exception as e:
        print(f"[FAIL] 任务 2: {e}")

    # 任务 3
    try:
        contacts = {"张三": {"phone": "13800138000", "city": "重庆"}}
        r = find_contact(contacts, "张三")
        assert r == ("13800138000", "重庆"), f"查找错误: {r}"
        r = find_contact(contacts, "王五")
        assert r is None, f"不存在应返回 None: {r}"
        score += 10
        print("[PASS] 任务 3")
    except Exception as e:
        print(f"[FAIL] 任务 3: {e}")

    # 任务 4
    try:
        contacts = {"张三": {"phone": "13800138000", "city": "重庆"}, "李四": {"phone": "13900139000", "city": "北京"}}
        r1 = delete_contact(contacts, "张三")
        assert r1 == True, f"删除成功应返回 True: {r1}"
        assert "张三" not in contacts, f"删除后不应存在张三: {contacts}"
        r2 = delete_contact(contacts, "王五")
        assert r2 == False, f"删除不存在应返回 False: {r2}"
        score += 10
        print("[PASS] 任务 4")
    except Exception as e:
        print(f"[FAIL] 任务 4: {e}")

    # 任务 5
    try:
        contacts = {"张三": {"phone": "13800138000", "city": "重庆"}}
        save_contacts("_day12_contacts.txt", contacts)
        with open("_day12_contacts.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()
        assert content == "张三,13800138000,重庆", f"保存格式: {content}"
        score += 10
        print("[PASS] 任务 5")
    except Exception as e:
        print(f"[FAIL] 任务 5: {e}")

    # 任务 6
    try:
        with open("_day12_contacts.txt", "w", encoding="utf-8") as f:
            f.write("张三,13800138000,重庆\n李四,13900139000,北京\n")
        loaded = load_contacts("_day12_contacts.txt")
        assert loaded == {"张三": {"phone": "13800138000", "city": "重庆"}, "李四": {"phone": "13900139000", "city": "北京"}}, f"读取错误: {loaded}"
        empty = load_contacts("_不存在_xyz.txt")
        assert empty == {}, f"文件不存在应返回空字典: {empty}"
        score += 10
        print("[PASS] 任务 6")
    except Exception as e:
        print(f"[FAIL] 任务 6: {e}")

    # 任务 7
    try:
        test_file = "_day12_flow.txt"
        if os.path.exists(test_file):
            os.remove(test_file)
        find_result, delete_result, loaded = full_flow(test_file)
        assert find_result == ("13900139000", "北京"), f"查找李四: {find_result}"
        assert delete_result == True, f"删除张三: {delete_result}"
        assert loaded == {"李四": {"phone": "13900139000", "city": "北京"}}, f"重新读取: {loaded}"
        if os.path.exists(test_file):
            os.remove(test_file)
        score += 10
        print("[PASS] 任务 7")
    except Exception as e:
        print(f"[FAIL] 任务 7: {e}")

    # 任务 8（需要人工交互，这里直接给分，请自己在终端测试）
    score += 10
    print("[PASS] 任务 8（请在终端单独测试菜单）")

    # 清理
    if os.path.exists("_day12_contacts.txt"):
        os.remove("_day12_contacts.txt")

    print(f"\n{'='*40}")
    print(f"  总分: {score} / 80")
    print(f"{'='*40}")
    if score >= 60:
        print("  小项目基础掌握得很扎实！")
    elif score >= 40:
        print("  基础概念清楚，个别地方需要巩固。")
    else:
        print("  建议先看一遍知识点文件再做题。")
    print(f"{'='*40}")
