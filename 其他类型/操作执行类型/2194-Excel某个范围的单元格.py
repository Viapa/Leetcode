def cellsInRange(s):
    """
    输入一个字符串s,格式类似于"A1: F3"，表示excel表中从A1单元格到F3单元格
    需要返回一个数组，包含从A1到F3中所有的单元格名称：["A1", "A2", "A3", "B1", ..., "F1", "F2", "F3"]
    请按递增顺序排列，先按行后按列
    :param s: 输入的字符串 [str]
    :return: 按顺序排列的数组 [List[str]]
    """
    s = s.split(":")
    min_num, max_num = min(s[0][1], s[1][1]), max(s[0][1], s[1][1])
    alpha1, alpha2 = s[0][0], s[1][0]
    ans = []
    # 遍历字母
    for col in range(ord(alpha1), ord(alpha2) + 1):
        for row in range(int(min_num), int(max_num) + 1):
            ans.append(chr(col) + str(row))

    return ans


# 测试
if __name__ == "__main__":
    s = "K1:M2"
    result = cellsInRange(s)
    print(f"经过处理, 字符串 {s} 的全体单元格数组为: {result} .")