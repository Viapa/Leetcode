def finalValueAfterOperations(operations):
    """
    给定一个字符串数组operations，每个元素包含对变量X的若干操作
    操作仅限于++X,X++,--X,X--四种
    X的初始值为0, 求执行完全部操作后的X值
    :param operations: 输入操作字符串数组 [List[str]]
    :return: 执行完操作后的X最终值 [int]
    """
    res = 0
    for action in operations:
        if "+" in action:
            res += 1
        else:
            res -= 1

    return res


# 测试
if __name__ == "__main__":
    operations = ["--X", "X++", "X++"]
    result = finalValueAfterOperations(operations)
    print(f"经过计算，经过所有操作后，X的最终值为: {result} .")