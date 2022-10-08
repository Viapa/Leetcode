# 定义二叉树
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_depth = 0  # 初始化-1层，因为根节点算第0层
        self.res = 0  # 结果变量

    def deepestLeavesSum(self, root):
        """
        给你一棵二叉树的根节点 root ，请你返回层数最深的叶子节点的和
        :param root: 二叉树根节点root [TreeNode]
        :return: 层数最深的叶子节点之和 [int]
        """

        # 解法：深度优先搜索-找出层数最深的节点并计算节点值之和
        # 从根节点开始遍历整个二叉树，遍历每个节点时需要记录该节点的层数，规定根节点在第0层。遍历过程中维护最大层数与最深节点之和
        # 1. 判断当前节点的层数与最大层数的关系：
        # (1) 如果当前节点的层数大于最大层数，则之前遍历到的节点都不是层数最深的节点，因此用当前节点的层数更新最大层数，并将最深节点之和更新为当前节点值
        # (2) 如果当前节点的层数等于最大层数，则将当前节点值加到最深节点之和
        # 2. 对当前节点的左右子节点继续使用深度优先搜索
        # 3. 全部遍历结束之后，即可得到层数最深叶子节点的和

        # 定义深度优先搜索
        def dfs(node, level):  # 传入：当前节点，当前节点层数，最大深度和累加和
            if node is None:  # 若当前节点为空, 则结束递归
                return
            if level > self.max_depth:  # 第一种情况
                self.max_depth = level
                self.res = node.val
            elif level == self.max_depth:  # 第二种情况
                self.res += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        # 初始化传入根节点
        dfs(root, 0)

        return self.res
