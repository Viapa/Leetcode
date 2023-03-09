"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
"""

"""
方法同二叉树的层序遍历大同小异，需要注意在res.append(level)时，改变一下队列level的元素顺序
具体而言，当遍历层为奇数时不变，当遍历层为偶数时，使用level.reverse(),就可以保证最后的遍历保存结果是锯齿形的
"""

def zigzagLevelOrder(root):
    if not root:
        return []

    queue = [root]
    res = []
    level_num = 1
    while queue:
        level = []
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_num % 2 == 0:
            level.reverse()
        res.append(level)
        level_num += 1

    return res
