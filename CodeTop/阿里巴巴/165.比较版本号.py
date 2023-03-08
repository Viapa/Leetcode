"""
给你两个版本号 version1 和 version2 ，请你比较它们。 
版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，
下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。 
比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果
版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 
0 和 1 ，0 < 1 。 返回规则如下： 

如果 version1 > version2 返回 1， 
如果 version1 < version2 返回 -1， 
除此之外返回 0

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"

输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2
"""

"""
使用python中list(map(int, v1.split('.')))可以将string变为list，并且去掉string中的前置0
然后根据v1_ls,v2_ls的长度，判断出哪一方需要末尾补零
在补零后，两个列表长度一致，遍历任意一个列表，逐一列表比较元素的值（相当于比较每个分割符内的值），按条件返回1,-1或0
"""


def compareVersion(version1, version2):
    v1_ls = list(map(int, version1.split('.')))
    v2_ls = list(map(int, version2.split('.')))
    n1, n2 = len(v1_ls), len(v2_ls)
    if n1 > n2:
        v2_ls += [0] * (n1 - n2)
    elif n1 < n2:
        v1_ls += [0] * (n2 - n1)
    for i in range(len(v1_ls)):
        if v1_ls[i] > v2_ls[i]:
            return 1
        elif v1_ls[i] < v2_ls[i]:
            return -1
    return 0
