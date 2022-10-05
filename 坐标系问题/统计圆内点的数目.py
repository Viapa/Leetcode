def countPoints(points, queries):
    """
    给定两个数组points和queries，分别代表点的坐标集合和圆的坐标集合
    其中，points[i]=[xi, yi]，表示点在二维坐标系的位置
    queries[j]=[xj, yj, rj]，表示圆在二维坐标系的坐标和半径r
    要求对于某个queries[j]，求出在第j个圆内d的点的数量（边界也算作圆内）
    answer[j]表示第j个查询的答案
    :param points: 点的坐标集合 [List[List[int]]
    :param queries: 圆的坐标集合 [List[List[int]]
    :return: 对于不同查询的圆内数量答案列表 List[int]
    """
    # 利用圆的距离公式，判断点和圆心距离d与r的大小关系
    ans = [0 for _ in range(len(queries))]

    for idx, circle in enumerate(queries):
        x0, y0, r0 = circle[0], circle[1], circle[2]
        for point in points:
            xi, yi = point[0], point[1]
            d_square = (xi - x0) ** 2 + (yi - y0) ** 2
            r_square = r0 ** 2
            if d_square <= r_square:
                ans[idx] += 1

    return ans


# 测试
if __name__ == "__main__":
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
    result = countPoints(points, queries)
    print(f"经过计算，对于圆内点数量的查询答案为: {result} .")