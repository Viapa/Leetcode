def garbageCollection(garbage, travel):
    """
    有三种垃圾车需要去不同房屋回收垃圾，garbage表示不同位置的房屋，garbage[i]表示房间里的垃圾
    垃圾分为三种，'M', 'P', 'G' 分别表示金属、纸张和玻璃
    三辆车均从起点开始，分别按次序（M->G）向房屋前进
    每回收任意一个垃圾需要1分钟，没有对应垃圾的屋子时，相对的车辆也可以不用前进
    travel表示不同屋子之间的距离，travel[0]表示从0到1屋子需要的时间
    请求出收拾完所有垃圾需要花费的最少总分钟数
    :param garbage: 不同房间的垃圾集合 [list[str]]
    :param travel:  不同屋子之间的距离 [list[int]]
    :return: 收拾完所有垃圾最少需要花费的时间（分钟） [int]
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