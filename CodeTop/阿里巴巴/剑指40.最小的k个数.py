"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

注：不能使用传统.sort()方法进行排序
"""

"""
本题目考察的是快速排序算法，即用快速排序的算法解决最小k个数问题。
将快速排序算法分为partition部分和sort部分：
前者用于对子数组arr进行基数的归位，返回的是基数的索引；后者作为递归排序
当对于最小K个数时，需要对前 k 个数进行排序，即返回的基数索引如果恰好表达第k个数（idx = k - 1)时，返回arr[:k]
当基数索引大于k-1时，应该继续对左侧归位，因为k-1位于左侧数字中；
当基数索引小于k-1时。应该继续对右侧归位，因为k-1位于右侧数字中

"""


class Solution(object):
    def getLeastNumbers(self, arr, k):
        def quick_sort(left, right):
            # 此处无需判断left=right
            # 因为如果left=right时，必然只有一个元素，且left排序刚好是k个元素
            if left > right:
                return None
            pivot = arr[left]
            i, j = left, right
            while i < j:
                while i < j and pivot <= arr[j]:
                    j -= 1
                arr[i] = arr[j]
                while i < j and pivot >= arr[i]:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot

            if i == k - 1:
                return arr[:i+1]
            elif i < k - 1:
                return quick_sort(i + 1, right)
            else:
                return quick_sort(left, i - 1)

        n = len(arr)
        if k > n:
            return arr
        elif k == 0:
            return []
        else:
            return quick_sort(0, n - 1)


if __name__ == "__main__":
    arr = [3, 2, 1, 4, 0]
    k = 3
    Init = Solution()
    res = Init.getLeastNumbers(arr, k)
    print(res)

