"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""


"""
需要注意，head节点代表的是1，而不是虚拟的head->1->2
本题利用前置节点，根据curr节点位置向前推n个节点为需要删除的节点，就可以找到倒数第n个节点位置
再利用prev.next = prev.next.next直接跳过该节点即可，最后返回虚拟头节点的next即为头节点位置.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummpy, prev = ListNode(0), ListNode(0)
    dummpy.next = head
    prev.next = dummpy
    curr = dummpy
    i = 0
    while curr:
        if i >= n:
            prev = prev.next
        i += 1
        curr = curr.next
    prev.next = prev.next.next

    return dummpy.next

