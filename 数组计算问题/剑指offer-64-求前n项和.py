def sumNums(n):
    """
    在不允许使用乘法、for、while等关键字字以及判断语句的前提下
    求1+2+3+...+n的值
    :param n: 输入末尾项n [int]
    :return: 求n项之和 [int]
    """
    # 等差数列求和公式
    return n * (n + 1) // 2


# 测试
if __name__ == "__main__":
    num = 9
    result = sumNums(num)
    print(f"经过计算: 1+2+3...+{num} 的和为: {result} .")