def CalCountPrimes(n):
    """
    给定整数n，求所有小于非负整数n的质数的数量
    :param n: 输入的正整数 [int]
    :return: 返回小于n的正整数数量 [int]
    """
    is_prime_ls = [True] * n  # 设定 [0, 1, 2, 3,..., n-1] 全是质数
    i = 2 # 从2开始计算
    while i**2 < n: # 对于sqrt(n)以下的数而言
        if is_prime_ls[i]:  # 如果是第一次见的质数
            for j in range(i**2, n, i): # 则取比i^2大的, i的倍数全都是合数, 步长为i(表示i的倍数)
                is_prime_ls[j] = False
        i += 1

    cnt = 0
    for is_prime in is_prime_ls[2:]: # 排除0和1
        if is_prime:
            cnt += 1

    return cnt


# 测试
if __name__ == "__main__":
    x = 120
    result = CalCountPrimes(x)
    print(f"通过计算: 小于 {x} 的质数有 {result} 个.")