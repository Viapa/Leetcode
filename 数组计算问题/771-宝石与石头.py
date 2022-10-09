def numJewelsInStones(jewels, stones):
    """
    拥有一个字符串jewels表示宝石类型，另一个字符串stones表示拥有的石头
    请求出拥有石头中，有多少是宝石（字符区分大小写）
    :param jewels: 宝石字符串 [str]
    :param stones: 石头字符串 [str]
    :return: 石头中宝石的数量 [int]
    """
    # 题目本身不难，关键在于优化（空间换时间）
    stone_dic = dict()
    for s in stones:
        stone_dic[s] = stone_dic.get(s, 0) + 1

    res = 0
    for item in jewels:
        res += stone_dic.get(item, 0)

    return res


# 测试
if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    result = numJewelsInStones(jewels, stones)
    print(f"经过计算，属于宝石的石头数量为: {result} .")