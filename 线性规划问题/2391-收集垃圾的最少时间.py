def garbageCollection(garbage, travel):
    """

    :param garbage:
    :param travel:
    :return:
    """
    timeCost = 0
    metalNum, paperNum, glassNum = 0, 0, 0
    metalDistance, paperDistance, glassDistance = 0, 0, 0
    for idx, item in enumerate(garbage):
        for i in item:
            if i == "M":
                metalDistance = idx
                metalNum += 1
            if i == "P":
                paperDistance = idx
                paperNum += 1
            if i == "G":
                glassDistance = idx
                glassNum += 1
    totalDistance = 0
    for step in range(len(travel)):
        if metalDistance > step:
            totalDistance += travel[step]
        if paperDistance > step:
            totalDistance += travel[step]
        if glassDistance > step:
            totalDistance += travel[step]

    timeCost = metalNum + paperNum + glassNum + totalDistance
    return timeCost

# 测试
if __name__ == "__main__":
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    result = garbageCollection(garbage, travel)
    print(f"经过计算，收拾完所有垃圾最少需要花费 {result} 分钟.")