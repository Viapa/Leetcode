def combinationSum(candidates, target):
    """
    给你一个 无重复元素的整数数组candidates和一个目标整数target，请找出candidates中可以使数字和为目标数target的所有不同组合，以列表形式返回。
    可以按任意顺序返回
    注意：candidates中的同一个数字可以无限制重复被选取。如果至少一个数字的被选数量不同，则两种组合是不同的。
    :param candidates: 数字候选集数组 [List[int]]
    :param target: 目标数字 [int]
    :return: 满足条件的所有组合 [List[List[int]]
    """
    res = []
    candidates.sort()  # 排序后可以剪枝

    def backtrack(pos, ans):
        # 条件判断1: 前数组和已大于目标:
        if sum(ans) > target:
            return
        # 条件判断2: 当前数组和等于目标:
        if sum(ans) == target:
            res.append(ans[:])
            return
        # 对所有数字进行遍历, 需要注意下一个搜索位置从当前pos开始，不是往后，也不是从头开始搜索
        for i in range(pos, len(candidates)):
            if sum(ans) + candidates[i] > target:  # 剪枝判断: 如果当前ans和大于target，则后续数字无需遍历（需要先对数组进行排序）
                break
            ans.append(candidates[i])
            backtrack(i, ans)
            ans.pop()

    backtrack(0, [])

    return res


# 测试
if __name__ == "__main__":
    candidates = [2, 3, 5]
    target = 8
    result = combinationSum(candidates, target)
    print(f"经过计算: 候选集 {candidates} 中和为 {target} 的组合有: {result} .")