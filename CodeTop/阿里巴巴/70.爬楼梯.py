"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

"""
最经典的动态规划问题：
设dp(n)为爬到第n阶楼梯所可能的全部方法，则dp(n) = dp(n-1) + dp(n-2)
表示可以由n-1阶楼梯爬一个到达，也可以是由n-2阶楼梯爬两个到达，则方法数为dp(n-1)加上dp(n-2)
初始化dp(0) = 0, dp(1) = 1, dp(2) = 2
"""


def climbStairs(n):
    if n < 2:
        return n
    dp = [0 for _ in range(n + 1)]  # dp可以设为0 ~ n 共 n+1 个
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n = 3
res = climbStairs(n)
print(res)