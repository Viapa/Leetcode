"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

"""
使用回溯法解决该问题：
（1）终止条件为tmp数组元素个数等于arr个数，此时往res中加入tmp，注意需要使用tmp[:]
原因：res.append(tmp) 这一句只是简单的浅拷贝，也就是往res中添加的是tmp的地址，并不是真正复制了一份。
当tmp改变时，随之在res中的值也会发生改变。所以res最后就保存了几个一模一样的值。
（2）循环次数为len(arr),但需要关注当前arr[i]元素是否已经被保存了，若已经存在则直接跳过本次循环
（3）接下来时回溯三个步骤：append() + backtrack + pop()
（4）回溯函数定义可以传入arr和tmp，分别表示当前遍历的数组和临时存储的数组结果
"""


def permute(nums):
    def backtrack(arr, tmp):
        if len(tmp) == len(arr):
            res.append(tmp[:])
            return None

        for i in range(len(arr)):
            if arr[i] in tmp:
                continue
            tmp.append(arr[i])
            backtrack(arr, tmp)
            tmp.pop()

    res = []
    backtrack(nums, [])
    return res