def quick_sort(arr, reversed=False):
    def recursive_sort(arr, left, right):
        if left >= right:
            return None
        else:
            pivot = arr[left]
            i = left
            j = right
            while i < j:
                while i < j and arr[j] > pivot:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot
            recursive_sort(arr, left, i - 1)
            recursive_sort(arr, i + 1, right)

    n = len(arr)
    recursive_sort(arr, 0, n - 1)
    if reversed:
        return arr[::-1]
    else:
        return arr


if __name__ == "__main__":
    arr = [5, 1, 2, 4, 6, 8, 3]
    res = quick_sort(arr)
    reversed_res = quick_sort(arr, reversed=True)
    print(res, reversed_res)
