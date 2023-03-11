"""
给定一个二叉树的根节点 root，返回 它的 中序 遍历 。
输入：root = [1,null,2,3]
输出：[1,3,2]
"""


"""
中序遍历需要先遍历左节点，然后是中间节点，最后才是右节点
可以使用回溯法，先传入node.left和当前结果res，再记录中间节点的值node.val,最后传入node.right和res即可实现
"""


def inorderTraversal(root):
    def backtrack(node, res):
        if node:
            backtrack(node.left, res)
            res.append(node.val)
            backtrack(node.right, res)

    res = []
    if not root:
        return res
    backtrack(root, res)

    return res

