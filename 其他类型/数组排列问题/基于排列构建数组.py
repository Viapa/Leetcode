def buildArray(nums):
    """
    构建一个数组，需要满足ans[i]=nums[nums[i]], nums是输入数组，ans是构建的数组
    :param nums: 输入一个数组 [List[int]]
    :return: 返回构建好的数组 [List[int]]
    """
    res = []
    for i in nums:
        res.append(nums[i])

    return res


# 测试
if __name__ == "__main__":
    arr = [5,0,1,2,3,4]
    result = buildArray(arr)
    print(f"经过变换，对于输入数组: {arr} 的构建数组为:")
    print(result)