def countKDifference(nums, k):
    """
    给你一个整数数组nums和一个整数k，请你返回数对(i, j)的数目，满足i < j且|nums[i] - nums[j]| == k
    :param nums: 输入数组 [List[int]]
    :param k: 给定整数 [int]
    :return: 满足条件的数对数目 [int]
    """
    # 与两数之和类似
    res = 0
    num_dict = dict()
    for num in nums:
        lower = num - k
        higher = num + k
        res += num_dict.get(lower, 0) + num_dict.get(higher, 0)
        num_dict[num] = num_dict.get(num, 0) + 1

    return res


# 测试
if __name__ == "__main__":
    nums = [1, 2, 2, 1]
    k = 1
    result = countKDifference(nums, k)
    print(result)