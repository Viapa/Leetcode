def permute(nums):
    """
    给定一个不含重复数字的整数数组 nums ，返回其所有可能的全排列
    如输入 nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    :param nums: 输入数组 [List[int]]
    :return: 输出全排列数组 [List[List[int]]
    """
    res = []

    # 使用回溯函数
    def backtrack(ans):
        if len(ans) == len(nums):
            res.append(ans[:])
            return
        for num in nums:  # 这里每次都要从头遍历元素，而不是一个定向的
            if num in ans:  # 判断元素是否已被当前数组保存
                continue
            else:
                ans.append(num)
                backtrack(ans)
                ans.pop()

    backtrack([])

    return res


# 测试
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permute(nums)
    print(f"经过计算: 数组 {nums} 的全排列为: {result} .")