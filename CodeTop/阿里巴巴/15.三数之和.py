"""
给定一个包含n个整数的数组nums, 判断nums中是否存在三个元素a,b,c，使得a+b+c=0？
请你找出所有和为0且不重复的三元组
如：输入nums=[-1,0,1,2,-1,-4]
输出: [[-1,-1,2], [-1,0,1]]
"""

"""
对数组排序后，使用外层遍历＋双指针方法，当前元素为nums[i]，在剩余数组nums[i+1:]中寻找res=0-nums[i]的两数，若能找到就记录，否则继续循环i
注意，i循环到n-3后停止，此时只剩两个元素；并且对于nums[i]和nums[i-1]需要比较数字是否相同，若相同直接跳过，避免造成重复记录
以下是用伪代码简单写的思路过程：
nums=[-1,0,1,2,-1,-4]
n = 6
nums.sort()
-> [-4, -1, -1, 0, 1, 2]

i = 0 
left = 1
right = n-1 = 5
res = 0-(-4) = 4

while left < right:
    if nums[left] + nums[right] = res: 
        return [nums[i], nums[left], nums[right]]
    elif nums[left] + nums[right] < res:   # 说明值太小，往大了找，右指针已经到边界，让左指针往后找
        left += 1
    else:  # 说明值太大，往小了找，左指针已经到边界，让右指针往前找
        right -= 1
    left += 1
    
i = 0, res = 4
while循环：
    第一次：left = 1, right = 5 -> left -> 2 -> 3 -> 4 -> 5 right = left 循环终止；
i = 1, res = 1
while循环：
    第一次：left = 2, right = 5 -> 满足条件： out.append([-1, -1, 2])
    第二次：left = 3, right = 5 -> tmp = 2 > res, 右指针左移， right -> 4, tmp = 1 = res，满足条件：out.append([-1, 0, 1])
    第三次：left = 4 = right 循环结束
i = 2, res = 1 与之前元素相同，若相同直接跳过, 否则就重复记录
i = 3, res = 0
while 循环：
    第一次：left = 4，right=5，tmp=3 右指针左移， right -> 4
    第二次：left = 4 = right，循环结束
i = 4, 在外层while循环判断：当i > n - 3时停止，此时必然只剩两个元素;

最后返回out.
"""

def threeSum(nums):
    n = len(nums)
    out = []
    if not nums or n < 3:
        return []
    nums.sort()
    for i in range(n-2):
        if nums[i] > 0:
            return out
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        res = 0 - nums[i]
        while left < right:
            if nums[left] + nums[right] == res:
                out.append([nums[i], nums[left], nums[right]])
                # 这里需要判断后面是否有重复组合
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 经过去重后,确保了left和right的下一个位置都是不重复的
                left += 1
                right -= 1
            elif nums[left] + nums[right] > res:
                right -= 1
            else:
                left += 1
    return out


if __name__ == "__main__":
    arr1 = [-4, -1, -1, 0, 1, 2]
    res1 = threeSum(arr1)
    print(res1)
    arr2 = [0, 0, 0, 0]
    res2 = threeSum(arr2)
    print(res2)