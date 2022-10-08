def xorOperation(n, start):
    """
    给定整数n和start，数组nums被定义为: nums[i] = start + 2*i 且 n == nums.length
    请返回 nums 中所有元素按位异或（XOR）后得到的结果。
    :param n: 数组的长度 [int]
    :param start: 构建数组的变量 [int]
    :return: 返回所有元素异或后的结果 [int]
    """
    # 只遍历一次即可
    arr = [None for _ in range(n)]
    res = 0
    for i in range(n):
        arr[i] = start + 2 * i
        res ^= arr[i]

    return res


# 测试
if __name__ == "__main__":
    n = 4
    start = 3
    result = xorOperation(n, start)
    print(f"经过计算，数组经过异或操作后的结果为: {result} .")