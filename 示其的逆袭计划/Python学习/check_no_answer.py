# -*- coding: utf-8 -*-
# 练习题"答案泄漏"检查器  (2026.9.7 新增)
# ============================================
# 用法:  python check_no_answer.py "xxx练习.py"
# 作用: 检查一个练习文件里,【提示/请在下方/期望】这类引导行
#       有没有混进"能直接运行的答案代码"(如 print(A@B)、h=W1@x+b1 等)。
#       一旦发现,退出码=1 并列出具体行——通不过就不要提交,回去改干净。
#
# 为什么写它: 反复出现的错误是"生成练习题时把答案写进正文或提示里"。
#   光靠自觉会漏,所以做成脚本强制检查。检查只针对【引导行】,
#   不会误伤题目自带的数据(A=np.array(...)、import 那些都在引导行之外)。
#
# 判定"答案代码"的规则(只对引导行生效,要求是【能运行的完整代码】):
#   print( 后面跟 ASCII 变量    → 例如 print(A @ B)、print(P.T)   —— 直接给出答案
#   ASCII变量 = 赋值            → 例如 h = W1@x+b1  (注意中文"得分 = ..."不算)
#   np.xxx(                    → 例如 np.where(...)          —— 直接可运行的调用
# 说明: 纯文字提示如"矩阵乘用 @"、"转置用 .T"、"得分 = 权重@输入 + 偏置"
#       只是描述概念,不用 ASCII 变量写成可运行代码 → 不会误判。
import re
import sys

BAD = re.compile(
    r'print\s*\([^)]*[A-Za-z_][^)]*\)'   # print( len( 等含 ASCII 变量的括号调用
    r'|np\.\w+\('                    # np.xxx(
)

# 只检查"引导行"（这些行不该出现代码）
GUIDE = ('提示', '请在下方', '期望', '任务', '答案')


def check(path):
    try:
        lines = open(path, encoding='utf-8').read().splitlines()
    except OSError as e:
        print(f"读文件失败: {e}")
        return 2

    leaks = []
    for i, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        # 只扫引导行
        if not any(g in line for g in GUIDE):
            continue
        body = line.lstrip('#').strip()   # 去掉行首注释符再看
        # 含 ? / ??? 占位符的→是"填坑模板"(hid了答案),不算泄漏,放过
        if '?' in body:
            continue
        if BAD.search(body):
            leaks.append((i, line))

    if leaks:
        print(f"[警告] {path} 检出 {len(leaks)} 处疑似答案泄漏(通不过,请改干净再提交):")
        for i, l in leaks:
            print(f"   行 {i}: {l}")
        return 1
    print(f"[通过] {path} 引导行无答案泄漏")
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python check_no_answer.py \"xxx练习.py\"")
        sys.exit(2)
    sys.exit(check(sys.argv[1]))
