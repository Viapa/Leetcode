"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
"""

"""
利用栈来存储正向的节点node，当栈长度等于k时，利用pop()函数来逆序输出节点
当然，需要利用prev和curr节点配合，prev用于翻转后的链接，curr用于当前节点的遍历
设置虚拟头节点dummpy用于最后返回
时间复杂度O(N/K*K)=O(N), 空间复杂度O(K)
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    if not head or k == 1:
        return head
    dummmy = ListNode(0)
    dummmy.next = head
    prev = dummmy
    curr = head
    stack = []
    while curr:
        stack.append(curr)
        curr = curr.next
        if len(stack) == k:
            next_start = stack[-1].next
            while stack:
                prev.next = stack.pop()
                prev = prev.next
            prev.next = next_start

    return dummmy.next




