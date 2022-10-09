def minOperations(boxes):
    """
    有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes
    其中 boxes[i] 的值为 '0' 表示第 i 个盒子是空的，而 boxes[i] 的值为 '1' 表示盒子里有1个小球。
    在一步操作中，你可以将1个小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子的相邻需满足 abs(i - j) == 1 。
    操作执行后，某些盒子中可能会存在不止一个小球
    返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的最少操作数
    :param boxes: 二进制字符串盒子 [str]
    :return: 将所有小球移动到盒子所需的最少操作数数组 [List[int]]
    """
    ans = [None for _ in range(len(boxes))]
    have_ball = []
    no_ball = []
    for idx, s in enumerate(boxes):
        if s == '1':
            have_ball.append(idx)
        else:
            no_ball.append(idx)

    for i in range(len(boxes)):
        tmp = 0
        for j in have_ball:
            tmp += abs(j - i)
        ans[i] = tmp

    return ans

# 测试
if __name__ == "__main__":
    boxes = "001011"
    result = minOperations(boxes)
    print(f"经过计算，将所有小球移动到盒子的最少操作数的数组为: {result} .")