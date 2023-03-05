"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

"""
1、构建一个hashMap，用于存储遍历到的字符串的最新位置
2、使用left变量限制当前无重复字符的子串起始位置，right变量为当前遍历位置，也是子串结束位置
3、使用right对输入字符串s进行遍历，若新字符在之前存在，且存在于当前统计的子串中，则更改left位置到最新，并更新字符最新位置
4、每次遍历最后判断一下无重复字符的最长字串长度
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pid_dict = dict()  # hashMap记录每个字符的最新位置
        max_length = 0  # 最长子串长度
        left = 0  # 当前子串起始位置
        for right in range(len(s)):  # 遍历字符串
            curr = s[right]  # 当前新字符
            if curr in pid_dict and pid_dict[curr] >= left:
                left = pid_dict[curr] + 1  # 子串起始位置更新为旧字符位置+1
            pid_dict[curr] = right  # 字符最新位置更新
            max_length = max(max_length, right-left+1)  # 比较最大长度

        return max_length


# 测试功能
if __name__ == "__main__":
    obj = Solution()
    s = "abcabcbb"
    res = obj.lengthOfLongestSubstring(s)
    print(res)

