"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""

"""
使用队列来解决层序遍历
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []

    queue = [root]  # 初始化队列
    res = []
    while queue:
        level = []  # 存储当前层节点的值
        size = len(queue)  # 当前层节点的数量
        # 遍历当前层所有的节点
        for i in range(size):
            node = queue.pop(0)  # 取出当前层的节点，并删除节点（当此处queue为空后表示当前层的节点都遍历完成）
            level.append(node.val)  # 将节点值存储到level
            if node.left:  # 如果节点的左子树存在
                queue.append(node.left)  # 队列加入左子树
            if node.right:  # 如果节点的右子树存在
                queue.append(node.right)   # 队列加入右子树
        res.append(level)

    return res


