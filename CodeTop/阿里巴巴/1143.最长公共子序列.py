"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
"""

"""
使用动态规划解决此问题，dp[i][j]表示，text1的前i个字符串和text2的前j个字符串的最长公共子序列；
先画出动态规划图：假设text1="adfg", text2="abcde"
  '' a b c d e
'' 0 0 0 0 0 0
a  0 1 1 1 1 1
f  0 1 1 1 1 1
d  0 1 1 1 2 2
g  0 1 1 1 2 2
左侧text1的第i个字符，上侧表示text2的第j个字符;
对于第一行，表示空字符串的公共子序列，当然都为0
对于第二行，表示text1的子串'a'和text2中的子串'a','ab','abc','abcd','abcde'的最长公共子序列，当然为1；
对于第三行，表示text1的子串'af'和text2中的子串'a','ab','abc','abcd','abcde'的最长公共子序列，计算可知也都为1；
对于第四行，表示text1的子串'afd'和text2中的子串'a','ab','abc','abcd','abcde'的最长公共子序列，观察可知对于'a','ab','abc'都是1，
但是第四个字符'd'刚好等于text1的字符'd'，因此公共子序列为2，后面'abcde'也是2；
对于最后一行，同理将数字补充完成，可知text1和text2的最长公共子序列就是右下角的数字2。
归纳上述规律，可以知道当text1[i]!=text2[j]时，dp[i][j]应该等于max(dp[i-1][j], dp[i][j-1])
当text1[i]=text2[j]时，dp[i][j]应该等于dp[i-1][j-1] + 1
最后返回dp[m][n], m是text1的长度，n是text2的长度，此问题得到解决。
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        if n == 0 or m == 0:
            return 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 字符串text1和text2的索引需要减1
                i_dx = i - 1
                j_dx = j - 1
                if text1[i_dx] == text2[j_dx]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]