def largestLocal(grid):
    """
    给定一个矩阵grid，需要生成一个大小为(n - 2) x (n - 2) 的整数矩阵maxLocal，并满足：
    maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的最大值
    换句话说，需要对矩阵图进行"卷积"操作
    :param grid: 输入原始矩阵 [List[List[int]]
    :return: 返回卷积后的矩阵 [List[List[int]]
    """
