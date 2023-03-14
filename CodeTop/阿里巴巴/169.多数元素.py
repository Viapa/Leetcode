"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

"""
使用“元素计数器”可以筛选出出现次数最多的元素
然后对该元素再次进行统计，可以知道是否为多数元素
其中，“元素计数器”可以由O(1)空间来实现：初始化一个候选数candidate和计数count
当count=0时，candidate=num[i]，若num==candidate，则count+=1，否则count-=1
遍历完全部数后，最终的candidate必为数组中出现次数最多的那个元素
"""


def majorityElement(nums):
    candidate = None
    count = 0
    n = len(nums)
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    major_num = 0
    for num in nums:
        if num == candidate:
            major_num += 1
    if major_num > (n //2):
        return candidate
    else:
        return None
