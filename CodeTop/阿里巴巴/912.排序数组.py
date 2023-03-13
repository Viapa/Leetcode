"""
给你一个整数数组 nums，请你将该数组升序排列
"""

"""
本题完全等同于考察快速排序，请参考快速排序解题方法。
时间复杂度O(logn)
"""


def sortArray(nums):
    def recursive_sort(nums, left, right):
        if left >= right:
            return None
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and pivot < nums[j]:
                j -= 1
            nums[i] = nums[j]
            while i < j and pivot >= nums[i]:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot

        recursive_sort(nums, left, i - 1)
        recursive_sort(nums, i + 1, right)

    n = len(nums)
    recursive_sort(nums, 0, n - 1)

    return nums


nums = [5, 1, 2, 4, 6, 8, 3]
res = sortArray(nums)
print(res)
