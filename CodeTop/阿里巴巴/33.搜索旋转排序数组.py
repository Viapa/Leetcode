"""
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""

"""
利用二分法，根据nums[mid]和nums[left]以及nums[right]的大小关系，先判断哪侧有序
然后在判断target是否在该有序区间内，从而对left和right进行变化
最终若有nums[mid]==target,则返回mid，否则当left>right后返回-1
"""


def search(nums, target):
    n = len(nums)
    if n < 1:
        return -1

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 若右半侧有序
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:  # 注意，是闭区间，但上面mid的对应值已经不等于target
                left = mid + 1
            else:
                right = mid - 1
        # 若左半侧有序
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1
