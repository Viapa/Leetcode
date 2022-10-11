def numIdenticalPairs(nums):
    """
    给你一个整数数组nums
    如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组"好数对"
    最后返回数组中好数对的数目
    :param nums: 输入数组 [List[int]]
    :return: 好数对的个数 [int]
    """
    # 本题主要考点在于优化，空间换时间
    num_dict = dict()
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1

    res = 0
    for k, v in num_dict.items():
        if v > 1:
            res += (v * (v -1) // 2)

    return res


# 测试
if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    result = numIdenticalPairs(nums)
    print(f"经过计算，数组 {nums} 中的好数对数目为: {result} .")