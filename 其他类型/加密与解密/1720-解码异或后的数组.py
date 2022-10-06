def decode(encoded, first):
    """
    给定一个经过编码的数组encoded和原数组的第一个元素first(=arr[0])
    编码数组encoded满足encoded[i] = arr[i] XOR arr[i+1], XOR表示"异或"运算关系
    如arr = [1, 0, 2, 1] -> encoded=[1, 2, 3]
    请解码返回原数组 arr
    :param encoded: 经过编码后的数组 [List[int]]
    :param first: 原数组arr的首个元素 [int]
    :return: 返回完整的原数组arr [List[int]]
    """
    arr = [None for _ in range(len(encoded) + 1)]
    arr[0] = first
    for idx, num in enumerate(encoded):
        arr[idx + 1] = arr[idx] ^ encoded[idx]  # 求原数组的对应元素，也是异或的结果

    return arr


#测试
if __name__ == "__main__":
    encoded = [6, 2, 7, 3]
    first = 4
    result = decode(encoded, first)
    print(f"经过计算，对于输入的编码后数组 {encoded} ,其对应的原始数组为: {result} .")