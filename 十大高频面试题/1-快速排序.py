def quick_sort(arr, reversed=False):
    def recursive_sort(arr, left, right):
        if left >= right:
            return None
        else:
            pivot = arr[left]
            i = left
            j = right
            while i < j:  # 大循环条件判断
                while i < j and arr[j] > pivot:  # 从右往左寻找比pivot小的数
                    j -= 1
                arr[i] = arr[j]   # 覆盖i元素的值
                while i < j and arr[i] <= pivot:  # 从左往右寻找pivot大的数
                    i += 1
                arr[j] = arr[i]  # 覆盖j元素的值
            arr[i] = pivot  # 将pivot放到中间位置，即此时i元素位置
            recursive_sort(arr, left, i - 1)  # 对pivot左侧元素的子数组进行递归排序
            recursive_sort(arr, i + 1, right)  # 对pivot右侧元素的子数组进行递归排序
    # 初始化执行快速排序
    n = len(arr)
    recursive_sort(arr, 0, n - 1)
    if reversed:  # 是否逆序写出
        return arr[::-1]
    else:
        return arr


if __name__ == "__main__":
    arr = [5, 1, 2, 4, 6, 8, 3]
    res = quick_sort(arr)
    reversed_res = quick_sort(arr, reversed=True)
    print(res, reversed_res)
