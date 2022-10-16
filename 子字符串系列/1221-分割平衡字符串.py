def balancedStringSplit(s):
    """
    对于字符串s，若元素"L"和"R"的数量相同，则称之为平衡字符串
    现在需要将给定字符串分割成尽可能多的平衡字符串
    注意：分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串
    返回可以通过分割得到的平衡字符串的最大数量
    :param s: 输入平衡字符串 [str]
    :return: 可以分割出平衡字符串的最大数量 [int]
    """
    n = len(s)
    # 注意，平衡字符串需要是连续的子串
    res = 0
    ans = 0
    for i in range(n):
        if s[i] == 'L':
            ans += 1
        else:
            ans -= 1
        if ans == 0:
            res += 1

    return res


# 测试
if __name__ == "__main__":
    s = "RLRRLLRLRL"
    result = balancedStringSplit(s)
    print(f"经过计算: 字符串 {s} 中的平衡字符串有 {result} 个 .")