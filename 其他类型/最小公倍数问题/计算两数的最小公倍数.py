def CalLeastCommonMultiple(x, y):
    """
    给定两个正整数x和y，求两个数的最小公倍数
    :param x: 输入正整数1 [int]
    :param y: 输入正整数2 [int]
    :return: 返回二者的最小公倍数 [int]
    """
    for t in range(1, y+1):
        res = x * t
        if res % y == 0:
            return res


# 测试
if __name__ == "__main__":
    a, b = 54, 24
    result = CalLeastCommonMultiple(a, b)
    print(f"通过计算: {a} 和 {b} 的最小公倍数是 {result} .")