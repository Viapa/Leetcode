"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
输入：s = "the sky is blue"
输出："blue is sky the"
请尝试使用 O(1) 额外空间复杂度
"""

"""
此题可以使用.split()方法，现将字符串倒序，然后依次倒序split后的单词即可，但空间复杂度为O(N)
若要实现O(1)的空间复杂度，则需要使用双指针法，具体如下：
(1) 先去掉s字符串中首尾的空格：s.strip()；
(2) 定义两个指针left=right=n-1,n为字符串s长度,res=""用于存储最终结果
(3) 当left>=0时进行循环，从末尾开始遍历，遍历每个单词的位置，即嵌套while循环，left-=1, 直到s[left]=" "时结束；
(4) 此时存储结果，将left+1到right的部分（即单词）按正常顺序添加到res中, 并在末尾加上空格
(5) 继续嵌套while循环，此时while的作用是过滤掉单词之间的空格，所以left-1，直到s[left]!=''时结束；
(6) 最后在每次循环结束前，将left赋值right，意味着下一个单词的末尾位置；
(7) 记得，最后需要去掉第一次循环时添加的末尾空格，return res.strip()
"""


def reverseWords(s):
    s = s.strip()
    n = len(s)
    left = right = n - 1
    res = ""
    while left >= 0:
        while left >= 0 and s[left] != ' ':
            left -= 1
        res += (s[left + 1: right + 1] + ' ')
        while left >= 0 and s[left] == ' ':
            left -= 1
        right = left

    return res.strip()
