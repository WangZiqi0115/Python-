"""
Day 8 · 词频统计示例 (基于 Day8 知识点第166行)
================================================
运行方式：在终端执行 python 词频统计示例.py
会创建一个示例文章文件，统计词频并打印结果。
"""

# ============================================================
# 第一步：创建一个示例文章文件
# ============================================================
article = """Python is a powerful programming language
Python is easy to learn
Programming in Python is fun
Learn Python every day"""

with open("示例文章.txt", "w", encoding="utf-8") as f:
    f.write(article)

print("✅ 已创建示例文章.txt")


# ============================================================
# 第二步：统计词频的函数（知识点第166行的完整版）
# ============================================================
def count_words(filename):
    """读取文件并统计词频，返回字典"""
    freq = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                words = line.strip().lower().split()
                for word in words:
                    freq[word] = freq.get(word, 0) + 1
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return {}
    return freq


# ============================================================
# 第三步：调用函数并展示结果
# ============================================================
result = count_words("示例文章.txt")

print("\n单词出现次数：")
for word, count in result.items():
    print(f"  {word}: {count}次")

print(f"\n共 {len(result)} 个不同的单词")

# 按出现次数从高到低排序
print("\n词频排名（从高到低）：")
ranked = sorted(result.items(), key=lambda x: x[1], reverse=True)
for i, (word, count) in enumerate(ranked, 1):
    print(f"  第{i}名：{word} — {count}次")
