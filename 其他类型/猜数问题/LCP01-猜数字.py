def game(guess, answer):
    """
    A,B在玩猜数字游戏，B每次会从1，2，3中选出一个，A也会从1，2，3中选一个猜
    共进行3轮游戏，请返回A猜中B选出的数字次数
    guess为A的猜测，answer为B的选择，长度均为3的数组
    :param guess: 猜测数组 [List[int]]
    :param answer: 答案数组 [List[int]]
    :return: 猜正确的次数 [int]
    """
    res = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            res += 1

    return res


# 测试
if __name__ == "__main__":
    guess = [2, 2, 3]
    answer = [3, 2, 1]
    result = game(guess, answer)
    print(f"经过计算，小A共猜中了 {result} 次.")