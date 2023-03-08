"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""


"""
使用字典存储元素和索引，每次遍历时寻找res=target-nums[i]是否存在于字典中
若存在则直接返回dict[res]和i；若不存在，字典加入nums[i]键和对应索引i
"""

def twoSum(nums, target):
    save_index = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in save_index:
            return [save_index[res], i]
        else:
            save_index[nums[i]] = i

    return -1


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums, target)
    print(res)


