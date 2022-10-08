def mostWordsFound(sentences):
    """
    一条句子由一些单词和空格组成，句子开头和结尾不会有空格
    给出一个句子集合sentence，sentence[i]表示单个句子
    请返回单个句子中单词的最多数目
    :param sentences: 输入句子集合 [List[str]]
    :return: 返回单一句子的单词最多数目 [int]
    """
    res = 0
    for idx, item in enumerate(sentences):
        wordCount = len(item.split(" "))
        if wordCount > res:
            res = wordCount

    return res


# 测试
if __name__ == "__main__":
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    result = mostWordsFound(sentences)
    print(f"经过计算，对于输入的句子集合，其最大的单词数为: {result} .")