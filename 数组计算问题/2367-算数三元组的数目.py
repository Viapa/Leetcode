def countTriplet(nums, diff):
    """
    给定一个严格递增的整数数组nums和一个正整数diff，若满足下列三个条件则三元组(i,j,k)是一个算数三元组
    1, i < j < k
    2, nums[j] - nums[i] == diff
    3, nums[k] - nums[j] == diff
    返回不同算数三元组的数目
    :param nums: 递增的整数数组 [List[int]]
    :param diff: 差值系数 [int]
    :return:  不同算数三元组的数量 [int]
    """
    # 根据规则 nums[i] = nums[j] - dff, nums[j] = nums[k] - diff, nums[i] = nums[k] - 2 * diff
    # 对于元素nums[i]，遍历后续数字，若nums[i] + diff > nums[?]时还没有一个数等于nums[i] + diff，则nums[i]被放弃
    # 因为无论如何num[i]也不能组合成公差为diff的等差数列;
    # 最简单的做法就是遍历每个数字，判断是否nums[i]+diff和nums[i]+2*diff同时存在于数组内，如果是res+=1，时间复杂度O(n^2)
    # 还有一种空间换时间做法，先取最大数字，然后从0开始建立字典键，值为个数（0或1），遍历原数组，记录所有存在的数字标记为1，不存在就是0
    # 然后在遍历字典，对于每一个数，检索它本身以及dict[i+diff]和dict[i+2*diff]值是否为1，如果满足res+=1, 时间复杂度O(m), 空间O(m), m是数组最大数
    # 基于此，字典存储只是判断是否有数，那么使用集合set()会更简单
    res = 0
    num_set = set(nums)
    for num in nums:
        if num + diff in num_set and num + 2 * diff in num_set:
            res += 1

    return res


# 测试
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 8, 9]
    diff = 2
    result = countTriplet(nums, diff)
    print(f"经过计算，不同算数三元组的数量共有 {result} 个.")