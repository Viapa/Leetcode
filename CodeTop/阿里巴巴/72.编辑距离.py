"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""

"""
使用动态规划法解决编辑距离问题：
设dp[i][j]为将word1的前i个字符变换为word2的前j个字符，所需要的最少操作数；
i=0，j=0 表示的是空字符串而不是第一个字符串，因此需要构建(m+1)*(n+1)的dp数组；
则dp[0][j]=j 表示将空字符串""，变换为word2的前j个字符，需要j步（都是添加）
以及dp[i][0]=i 表示将word1的前i个字符变换为空字符串""，需要i步（都是删除）
此外，当dp[i-1][j-1] 变换到 dp[i][j]时需要判断word1[i]是否等于word2[j],
因为 如果通过前序变换，word1的前i-1个字符可以变成word2的前j-1个字符时，并且word1的第i个字符还等于word2的第j个字符，说明此处不需要变换；
否则，应该考虑的是dp[i-1][j-1],dp[i-1][j]和dp[i][j-1]三种情况变换的最少步数再加上1即可。
"""


def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n+1) for i in range(m+1)]
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            # word中索引是dp索引减1
            i_ = i - 1
            j_ = j - 1
            if word1[i_] == word2[j_]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]



