def shuffle(nums, n):
    """
    给定一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列
    请将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组
    :param nums: 输入原始数组 [List[int]]
    :param n: x,y独立个数 [int]
    :return: 重新排列后的数组 [List[int]]
    """
    # 使用两个变量i和j，分别作为nums和新数组arr的索引指针
    arr = [None for _ in range(2 * n)]
    j = 0
    for i in range(n):
        arr[j] = nums[i]
        arr[j+1] = nums[i+n]
        j += 2

    return arr


# 测试
if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    result = shuffle(nums, n)
    print(f"经过处理，原数组 {nums} 经过重排后的数组为: {result} .")