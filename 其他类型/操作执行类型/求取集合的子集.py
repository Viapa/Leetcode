def getSubet(nums):
    """
    输入一个数组，返回这个数组的全部子集
    :param arr: 输入数组为整数集合 List[int]
    :return:  返回数组为子集的集合 List[List[int]]
    """
    # 此处介绍基于回溯法求子集的方法(包含空集）
    # 定义一个回溯函数，传入结果数组res，临时数组tmp，原数组nums和位置参数pos
    def subset_helper(res, tmp, nums, pos):
        res.append(tmp[:])  # 每次加入当前的临时数组内容，[:]表示复制
        for i in range(pos, len(nums)):  # 对pos位置之后进行遍历
            tmp.append(nums[i])  # 添加对应位置的元素到临时数组
            subset_helper(res, tmp, nums, i+1)  # 递归调用，位置pos需要加1
            tmp.pop()  # 临时数组进行回溯
        return

    tmp, res = [], []  # 初始化数组
    idx = 0  # 初始化位置
    subset_helper(res, tmp, nums, idx)

    return res


# 测试
if __name__ == "__main__":
    nums = [1, 2, 3, 5]
    result = getSubet(nums)
    print(f"经过计算，数组 {nums} 的所有子集有: {result} .")