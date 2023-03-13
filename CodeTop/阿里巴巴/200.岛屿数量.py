"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
"""

"""
使用深度优先搜索dfs解决该问题：
对每一行每一列的格子，先判断是否为陆地"1"，则开始寻找该格子四周相连的其他格子是否都为1，并记录下探索过的格子，将其变为0
递归结束条件为搜索位置已超过边界或者探索到了不为1的水部分
这样一来，对于相连一片的陆地，每次仅记一次，即为岛屿的数量。
最后返回所有记录之和即可。
"""


def numIslands(grid):
    def dfs(grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1'):
            return None
        grid[i][j] = '0'
        dfs(grid, i + 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)

    n = len(grid)
    m = len(grid[0])
    num_islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(grid, i, j)

    return num_islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
res = numIslands(grid)
print(res)

