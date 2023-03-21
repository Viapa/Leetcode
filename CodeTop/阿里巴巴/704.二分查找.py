"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
"""

"""
注意，只有当数组是升序的情况下才可以使用二分查找
使用left和right指针，每次计算mid位置以及更新left和right
利用while循环解决二分查找问题
"""


def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
