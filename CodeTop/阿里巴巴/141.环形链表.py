"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。
"""


"""
使用快慢指针法，定义fast和slow两个指针，fast按步长2遍历，slow按步长1遍历
当fast和slow相遇时说明有环，此外均无环
判断条件可以写为:fast.val == slow.val and fast.next == slow.next
注意在遍历和循环时，对于next节点的None判断
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    fast = head
    slow = head
    while fast:
        if fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val and fast.next == slow.next:
                return True
        else:
            return False

    return False