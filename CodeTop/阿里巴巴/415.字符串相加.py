"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
输入：num1 = "456", num2 = "77"
输出："533"
"""

"""
使用模拟加法解决字符串相加的问题：
从两个字符串的最后一位开始计算，用字典将字符映射为整数，然后进行加法运算；
此间会产生进位，所以还需要添加进位变量carry, 每次加和是s1+s2+carry，并产生新的进位
res中只存储每次计算的个位部分，可以用%10实现
循环指针左移，直到字符串遍历完以及进位归零（没有字符了就将值置为0）
最后返回res的倒序，因为是从个位开始添加结果的
"""


def addStrings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    res = []
    str2int = {str(i): i for i in range(10)}
    while i >= 0 or j >= 0 or carry > 0:
        left = str2int[num1[i]] if i >= 0 else 0
        right = str2int[num2[j]] if j >= 0 else 0
        tmp = left + right + carry
        carry = tmp // 10
        val = str(tmp % 10)
        res.append(val)
        i -= 1
        j -= 1

    res = "".join(res[::-1])
    return res
