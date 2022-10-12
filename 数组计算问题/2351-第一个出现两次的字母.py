def repeatedCharacter(s):
    """
    给一个由小写字母组成的字符串s，请找出并返回第一次出现两次的字母
    :param s: 输入字符串 [str]
    :return: 返回第一次出现两次的字母 [str]
    """
    # 简单题，循环一次
    s_dic = {}
    for c in s:
        s_dic[c] = s_dic.get(c, 0) + 1
        if s_dic[c] == 2:
            return c
        else:
            continue


# 测试
if __name__ == "__main__":
    s = "abccbaacz"
    result = repeatedCharacter(s)
    print(f"经过计算，字符串 {s} 中首次出现两次的字母为: {result} .")