"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
"""

"""
先理解题目，二叉树的直径指的是任意两个节点路径的最大长度而不是过根节点的最大长度
本题使用递归法比较容易实现，思路如下：
（1）直径本质上是二叉树节点深度的加和，即左子树深度+右子树深度+1即为某节点的直径
（2）子树的深度又可以使用递归法来实现，不停对左右子树进行遍历，碰上叶子节点后返回，节点的深度应该是左子树深度和右子树深度的较大一方
（3）用一个变量diameter来保存最大长度，每次对节点递归后，计算当前节点直径，最后保留的最大值即为二叉树的直径
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        # 初始化节点的最大直径
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        # 计算节点深度的方法(包含该节点）
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            return max(left_depth, right_depth) + 1

        # 计算节点直径的方法
        def dfs(node):
            if not node:
                return 0
            left_tree_depth = depth(node.left)
            right_tree_depth = depth(node.right)
            diameter = left_tree_depth + right_tree_depth + 1
            if diameter > self.max_diameter:
                self.max_diameter = diameter
            dfs(node.left)
            dfs(node.right)
            return None

        dfs(root)
        return self.max_diameter - 1
