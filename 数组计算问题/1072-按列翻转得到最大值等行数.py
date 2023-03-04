def solution(matrix):
    """
    给定一个m*n的矩阵matrix，可以从中选取任意数量的列并翻转其上的每个单元格
    翻转后单元格值从0变为1或从1变为0（矩阵中只有这两个值）
    求，当经过一些翻转后，行与行之间所有值都相等的最大行数
    :param matrix: 输入的矩阵 [List[int]]
    :return: 行值相等的行数 [int]
    """
