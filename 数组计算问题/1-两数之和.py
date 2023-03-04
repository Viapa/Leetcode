def twoSum(nums, target):
    """
    给出一个数组nums，target为目标，找出nums中和为target的两个数的索引并范返回
    :param nums: 输入数组 [List[int]]
    :param target: 目标和 [int]
    :return: 符合条件的数的索引 [List[int]]
    """
    # 经典空间换时间，用一个字典去保存索引，键为数值，值为索引
    # 只需要遍历一次数组，每次遍历的时候，找寻字典中是否存在target-num[i]的键，如果存在就返回当前索引和对应的字典值
    idx_dict = {}
    for idx, num in enumerate(nums):
        another = target - num
        if idx_dict.get(another) != None:
            return [idx_dict.get(another), idx]
        else:
            idx_dict[num] = idx
    return


# 测试
if __name__ == "__main__":
    nums = [2, 6, 15, 11, 19, 7]
    target = 9
    result = twoSum(nums, target)
    print(result)