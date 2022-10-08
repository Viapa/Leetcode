def minimumSum(num):
    """
    给出一个四位数num, 将num拆成两个全新的整数new1，new2（可以包含先导0）
    例如，num=2932，数位有两个2，一个9和一个3，拆出的new1和new2可以是[22,93], [232, 9], [2, 329]等
    请返回所有new1和new2之和的最小值
    :param num: 输入待拆出的四位数 [int]
    :return: new1和new2之和的最小值 [int]
    """
    # 将num转为字符串后排序:[x1,x2,x3,x4], 最小值应为[x4x3] + [x3x2]
    arr_str = [i for i in str(num)]
    arr_str.sort(reverse=True)
    new1 = int(arr_str[3] + arr_str[0])
    new2 = int(arr_str[2] + arr_str[1])

    return new1 + new2


# 测试
if __name__ == "__main__":
    num = 2932
    result = minimumSum(num)
    print(f"经过计算，四位数 '{num}' 经过拆分后的最小值为: {result} .")