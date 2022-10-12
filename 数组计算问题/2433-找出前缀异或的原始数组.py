def findArray(pref):
    """
    给定一个长度为n的整数数组pref, 请找出并返回满足下列条件，长度为n的数组arr
    条件为：pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
    注：arr的结果必然唯一
    :param pref:  输入数组 [List[int]]
    :return:  满足条件的数组 [List[int]]
    """
    # arr[0] = pref[0]
    # arr[0] ^ arr[1] = pref[1]
    # arr[0] ^ arr[1] ^ ... ^ arr[i] = pref[i], 异或具有交换性
    # arr[i] = arr[0] ^...^ arr[i-1] ^ pref[i]
    n = len(pref)
    arr = [None for _ in range(n)]
    arr[0] = pref[0]
    for i in range(n):
        if i == 0 :
            tmp = arr[0]
        else:
            arr[i] = tmp ^ pref[i]
            tmp ^= arr[i]

    return arr


# 测试
if __name__ == "__main__":
    nums = [5, 2, 0, 3, 1]
    result = findArray(nums)
    print(f"经过计算，数组 {nums} 中对应的条件数组为: {result} .")