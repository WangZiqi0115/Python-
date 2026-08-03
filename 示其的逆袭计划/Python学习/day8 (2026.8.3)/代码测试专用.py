"""
代码测试专用
=============
在这里随便写代码测试想法，不用担心弄坏其他文件。
"""

# print("Day 8 准备就绪！")
# try:
#     risky_code()
# except Exception as e:
#     print("出错了：", e)
def write_and_read(filename, lines):
    """
    write_and_read("test.txt", ["a", "b"]) -> ["a", "b"]
    """
    # 请在此处编写代码
    with open(filename,"w",encoding="utf-8") as fin:
        for word in lines:
            fin.write(f"{word}\n")
    with open(filename,"r",encoding="utf-8") as fout:
        line = [line.strip() for line in fout if line.strip()]
    return line
# with open("测试.txt","w",encoding="utf-8") as f:
#     f.write("张三,95\n李四,87\n王五,92")
name = []
score = []
with open("测试.txt","r",encoding="utf-8") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",") 
                name.append(parts[0])
                score.append(parts[1])

print(name,round(sum(int(x)for x in score) / len(score),1))
    
    # score = [n.strip().split(",")[1] for n in f if n.strip()]
    # s = 0
    # for num in score:
    #     new_num = int(num)
    #     s += new_num
    # print(s)

#     lst = []
# for data in line:
#     new_data = data.split(",")
#     lst.append(new_data)

# name = []
# for i in range(len(lst)):
#     name.append(lst[i][0])
# print(name)