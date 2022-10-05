def groupThePeople(groupSizes):
    """
    对n个人分为若干的组，输入人群数组groupSizes，其中 groupSizes[i] 是第 i 个人所在的组的大小
    需要返回一个列表，使得每个人i都在一个大小为 groupSizes[i] 的组中
    例如，groupSizes = [2,1,3,3,3,2]，2分为一个组1，容量为2，1分为一个组，容量为1，3分为一个组，容量为3
    则返回[[0, 5], [1], [2, 3, 4]]
    :param groupSizes: 输入待分组得人群列表 [List[int]]
    :return: 返回一个有效解列表 [List[List[int]]
    """
    # 利用字典统计每个独特的数字出现的索引列表
    ans = []
    numDict = dict()
    for idx, item in enumerate(groupSizes):
        if item not in numDict.keys():
            numDict[item] = []
        arr = numDict[item]
        if len(arr) >= item:
            ans.append(arr)
            numDict[item] = []
        numDict[item].append(idx)
    # 最后对缓存在字典中的数组进行再次提取
    for value in numDict.values():
        ans.append(value)

    return ans


# 测试
if __name__ == "__main__":
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    result = groupThePeople(groupSizes)
    print(f"经过计算，对于输入人群的一个有效分组为: {result} .")