"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为6 。
"""

"""
先判断是否单元素数组
利用i和j指针，i为子数组开始位置，j=i+1，向右遍历j
根据当前的子数组和tmp是否大于零和下一个元素是否比上一个元素大来判断是否需要更新子数组开始位置
即当tmp < 0 and nums[j] > nums[j-1]可以更新为i=j,j=i+1(自己验证原理）
若不满足上述条件，继续遍历j到下一个位置，同时tmp+=nums[j]
使用while循环，让i和j都进行循环中，任意一个到达末尾即停止
每次循环，比较并更新最大子数组和max_sum
"""


def maxSubArray(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n >= 2:
        max_sum = nums[0]
        tmp = nums[0]
        i = 0
        j = i + 1
        while i <= n - 1 and j <= n - 1:
            if tmp < 0 and nums[j] > nums[j-1]:
                i = j
                j = i + 1
                tmp = nums[i]
            else:
                tmp += nums[j]
                j += 1
            max_sum = max(tmp, max_sum)

        return max_sum
