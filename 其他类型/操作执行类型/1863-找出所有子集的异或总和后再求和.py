def subsetXORSum(nums):
    """
    一个数组的异或总和定义为数组中所有元素按位XOR的结果；如果数组为空，则异或总和为0
    例如，[2,5,6] 的异或总和为"2 XOR 5 XOR 6" = 1
    给你一个数组 nums ，请你求出 nums 中每个子集的异或总和，计算并返回这些值相加之和
    注意：元素相同的不同子集应多次计数
    :param nums: 输入的数组 [List]
    :return: 数组子集的异或和的总和
    """
    # 这里使用回溯法（数学法太复杂）: 先求出所有子集，然后遍历子集求取异或值之和
    def subset_helper(res, tmp, nums, pos):
        res.append(tmp[:])  # 每次加入当前的临时数组内容，[:]表示复制
        for i in range(pos, len(nums)):  # 对pos位置之后进行遍历
            tmp.append(nums[i])  # 添加对应位置的元素到临时数组
            subset_helper(res, tmp, nums, i+1)  # 递归调用，位置pos需要加1
            tmp.pop()  # 临时数组进行回溯
        return
    tmp, subset = [], []  # 初始化数组
    idx = 0  # 初始化位置
    subset_helper(subset, tmp, nums, idx)  # 获取全部子集

    ans = 0  # 定义返回值
    for idx, item in enumerate(subset):
        p = 0
        for ele in item:  # 求每个子集的异或值
            p ^= ele
        ans += p  # 累加

    return ans


# 测试
if __name__ == "__main__":
    nums = [3, 4, 5, 6, 7, 8]
    result = subsetXORSum(nums)
    print(f"经过计算，数组 {nums} 经过所有操作后得到的异或总和为: {result} .")
