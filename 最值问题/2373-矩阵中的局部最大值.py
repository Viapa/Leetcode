def largestLocal(grid):
    """
    给定一个矩阵grid，需要生成一个大小为(n - 2) x (n - 2) 的整数矩阵maxLocal，并满足：
    maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的最大值
    换句话说，需要对矩阵图进行"最大池化"操作
    :param grid: 输入原始矩阵 [List[List[int]]
    :return: 返回最大池化后的矩阵 [List[List[int]]
    """
    def maxPooling(pos_x, pos_y):  # 定义求局部3*3矩阵的最大值
        pos_max = -1
        for i in range(pos_x, pos_x + 3):
            row_max = 0
            for j in range(pos_y, pos_y + 3):
                if grid[i][j] > row_max:
                    row_max = grid[i][j]
            if row_max > pos_max:
                pos_max = row_max
        return pos_max

    n = len(grid)
    res = [[None for _ in range(n - 2)] for _ in range(n - 2)]

    X = 0  # 行位置参数
    while X < n - 2 :
        Y = 0  # 列位置参数
        while Y < n - 2:
            res[X][Y] = maxPooling(X, Y)
            Y += 1
        X += 1

    return res


# 测试
if __name__ == "__main__":
    grid = [[9, 9, 8, 1],
            [5, 6, 2, 6],
            [8, 2, 6, 4],
            [6, 2, 2, 2]]
    result = largestLocal(grid)
    print(f"经过计算，矩阵 {grid} 经过最大池化后得到的新矩阵为: {result} .")
