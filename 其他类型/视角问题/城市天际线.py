def maxIncreaseKeepingSkyline(grid):
    """
    在不改变从任何主要方向观测到的城市”天际线“的前提下，返回建筑物可以增加的最大高度增量总和
    所谓"天际线"是值从某个角度观察到的高度最大值:
    如[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 从北侧看的最大高度为[7, 8, 4, 9]
    :param grid: 输入的二维矩阵 [List[List[int]]]
    :return: 返回的天际线增量值 [int]
    """
    n = len(grid)
    # 先找到每一行, 每一列的最大值数组
    row_max_ls = []
    col_max_ls = []
    for i in range(n):
        max_row = grid[i][0]
        max_col = grid[0][i]
        for j in range(n):
            if grid[i][j] > max_row:
                max_row = grid[i][j]
            if grid[j][i] > max_col:
                max_col = grid[j][i]
        row_max_ls.append(max_row)
        col_max_ls.append(max_col)
    # 再根据连个列表进行遍历，求min[i, j]值作为增量矩阵, 同时减去对应grid中的值进行累加
    cnt = 0
    for i in range(n):
        for j in range(n):
            uplift = min(row_max_ls[i], col_max_ls[j])
            if grid[i][j] < uplift:
                cnt += uplift - grid[i][j]

    return cnt


# 测试
if __name__ == "__main__":
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    result = maxIncreaseKeepingSkyline(grid)
    print(f"通过计算: 在城市建筑物grid可以增加的最大高度增量总和为: {result} .")