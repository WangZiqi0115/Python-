# utils.py — 通用工具模块（Day 9 练习 6 使用）

def get_avg(scores):
    """返回成绩列表的平均分"""
    return sum(scores) / len(scores)


def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"


if __name__ == "__main__":
    # 只有直接运行 utils.py 时才执行
    print(get_avg([90, 80, 100]))
    print(get_grade(95))
