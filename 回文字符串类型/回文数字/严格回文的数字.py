def isStrictlyPalindromic(n):
    """
    给定正整数n，如果n在b进制下对应的字符串全都是回文的，则返回true，否则返回false；
    b为2到n-2中的所有整数；
    回文字符串是一种从前往后读和从后往前读都一样的字符串
    :param n: 输入的正整数n [int]
    :return: 是否构成回文 [bool]
    """
    # 此题一定为false，原理如下：
    # 假设n用商q和余数p表示为: n = qb + p, 由于题目说n-2进制也需要满足回文串
    # 则b可以取n-2, 然后看q和p的值写出进制数：如数字9在7进制下表示为12, 因为9/7商1余2
    # 所以, n = q(n-2) + p => [q=1, p=2] 是唯一解
    # 那么n-2进制下的表示必然为"12", 显然不是回文数
    # 另外, 还需要验证边界情况: 2 <= n-2, n >= 4; 当n=4时, 2进制表示为"100", 也不是回文数
    # 综上, 此题答案一定为False
    return False


# 测试
if __name__ == "__main__":
    x = 9
    result = isStrictlyPalindromic(x)
    print(f"通过计算: 正整数 {x} 是否为严格回文数字 -> {result} .")