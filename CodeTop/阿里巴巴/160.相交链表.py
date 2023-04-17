"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2,
skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
"""

"""
获取两个链表的长度，并将它们对齐。如果一个链表比另一个长，则将短链表前面加上若干个空节点，使两个链表长度相同。
同时遍历两个链表，比较它们的值是否相等。如果相等，则说明它们相交，返回该节点。否则，继续遍历直到遍历完整个链表，返回null
在代码中，首先遍历了两个链表，获取它们的长度并将它们对齐。然后同时遍历两个链表，比较它们的值是否相等，直到找到相交节点或者遍历完整个链表。
即，通过将两个链表对齐，然后同时遍历来判断它们是否相交。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        nodeA, nodeB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                nodeA = nodeA.next
        else:
            for i in range(lenB - lenA):
                nodeB = nodeB.next
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None