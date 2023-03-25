"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"
"""

"""
将数组中第一个字符串记为最长公共前缀探索的字符串，即最多也就这个字符串的长度；
然后遍历字符串中的前i个子串标记为当前前缀，再遍历其他字符串，比较它们的前i个字符子串
若遍历能完成，说明后面的n-1个字符串的前i个子串都与第一个字符串相同，此时可以更新最长公共前缀
否则，任意一个字符串的前i个子串与第一个字符串不相同，直接跳过循环，返回最长公共前缀，后面的不用遍历了。
时间复杂度最高O(MN)
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        base_str = strs[0]
        length = len(base_str)
        max_prefix = ""
        for i in range(length + 1):  # 这里需要注意，需要取到字符串最后一位
            prefix = base_str[:i]
            for j in range(n):
                curr_prefix = strs[j][:i]
                if curr_prefix != prefix:
                    return max_prefix
            max_prefix = prefix

        return max_prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    Solution = Solution()
    res = Solution.longestCommonPrefix(strs)
    print(res)