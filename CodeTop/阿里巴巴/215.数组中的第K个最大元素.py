"""
给定整数数组nums和整数k，请返回数组中第k个最大的元素。
请注意，需要寻找数组排序后的第k个最大元素
"""

"""
1、使用快速选择法进行解决
2、对于一个数组，取第一个元素为基数pivot，找出三部分子数组：right、left、mid，分别代表比pivot大的数，比pivot小的数和等于pivot的数
3、若k值小于等于right数组，说明在right数组里必然有第k大的数，此时递归right，继续传入k；
4、若k值小于right并且小于right+mid数组，说明在大于pivot和等于pivot都找不到第k大的数，此时递归left，传入k-len(right)-len(mid)；
需要说明一下，当在全部数组找第k大数时，若都不在right和mid中，那势必在left中。对left而言，相当于寻找left中的第k-len(right)-len(mid)大的数；
举个例子，从[3,1,2,5,5,6,4]中，寻找第6大的数，显然都不在right[5,5,6,4]和mid[3]中，必然在left[1,2]中。而对于left[1,2]需要寻找的是第6-4-1=1大的数而不是第6大的数;
5、若k都不满足上述条件，必然是由于right数组不够多，加上mid又过多导致的，那么就肯定在mid数组里，mid数组就是pivot组成的全部相同的数，所以取mid[0]即可。
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        lower = []
        mid = []
        higher = []
        for i in nums:
            if i < pivot:
                lower.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                higher.append(i)

        if k <= len(higher):
            return self.findKthLargest(higher, k)
        elif k > len(higher) + len(mid):
            return self.findKthLargest(lower, k - len(higher) - len(mid))
        else:
            return mid[0]


if __name__ == "__main__":
    arr = [3, 1, 2, 5, 5, 6, 4]
    k = 4
    obj = Solution()
    res = obj.findKthLargest(arr, k)
    print(res)
