def countMatches(items, ruleKey, ruleValue):
    """
    给定一个数组items，其中items[i]=[typei,colori,namei]，用于描述物品的类型、颜色和名称
    再给出两个字符串ruleKey,ruleValue，表示检索规则
    如果第i件物品能满足以下条件之一，则认为物品与检索规则是匹配的：
    1，ruleKey=="type" & ruleValue==typei
    2，ruleKey=="color" & ruleValue==colori
    3，ruleKey=="name" & ruleValue==namei
    请返回满足条件的物品数量
    :param items: 物品数组 [List[List[str]]
    :param ruleKey: 规则键字符串 [str]
    :param ruleValue: 规则值字符串 [str]
    :return: 匹配检索的物品数 [int]
    """
    if ruleKey == "type":
        idx = 0
    elif ruleKey == "color":
        idx = 1
    else:
        idx = 2
    res = 0
    for item in items:
        if item[idx] == ruleValue:
            res += 1

    return res


# 测试
if __name__ == "__main__":
    items = [["phone", "blue", "pixel"],
             ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    result = countMatches(items, ruleKey, ruleValue)
    print(f"经过计算，匹配的物品数共有 {result} 个.")