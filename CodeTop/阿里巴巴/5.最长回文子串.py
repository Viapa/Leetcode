"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
"""


"""
动态规划问题，用dp[i][j]表示字符串的第i个字符到第j个字符是否为回文串
判断条件有以下几种情况：
（1）dp[i][j] = True, where i = j;
（2）dp[i][j] = s[i] == s[j], where j = i + 2
（3）dp[i][j] = dp[i+1][j-1] && s[i] == s[j], where j - i > 2
然后每次比较当前的回文串是否为最大长度，同时记录下最长回文串的索引，届时返回即可
"""


def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]  # 构建一个n*n的dp数组
    max_lenth = 1  # 记录回文子串最大长度
    start = 0  # 记录回文子串起点索引位置
    # 遍历i和j，注意只有当i小于等于j时dp[i][j]才有讨论的意义
    for j in range(0, n):
        for i in range(0, j+1):  # 保证i<=j即可
            if j - i <= 2:  # 根据i和j条件不同判断情况
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])

            tmp_lenth = j - i + 1   # 当前子串长度
            if dp[i][j] and tmp_lenth > max_lenth: # 判断最大长度是否需要更新
                max_lenth = tmp_lenth
                start = i  # 同时也要更新最大字串的起始位置

    return s[start: start + max_lenth]






s = "babad"
print(longestPalindrome(s))