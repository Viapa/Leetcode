"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""

"""
结合k个一组翻转链表的题目，需要在left位置才开始往stack中加入node
然后当stack长度等于right-left+1时，开始pop和翻转
并且在清空stack时break循环（后面节点不需要变动）
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    k = right - left + 1
    i = 1
    stack = []
    while curr:
        if i < left:
            prev = prev.next
            curr = curr.next
            i += 1
            continue
        stack.append(curr)
        curr = curr.next
        if len(stack) == k:
            next_node = stack[-1].next
            while stack:
                prev.next = stack.pop()
                prev = prev.next
            prev.next = next_node
            break

    return dummy.next

