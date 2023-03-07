# 定义节点结构
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 定义反转链表
def reverseListNode(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


if __name__ == "__main__":
    # 定义原链表
    head = ListNode()
    first_node = ListNode(val=1)
    second_node = ListNode(val=2)
    third_node = ListNode(val=3)
    fourth_node = ListNode(val=4)
    head.next = first_node
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = None
    dummpy = head
    print("This is original ListNodes: ")
    while dummpy:
        print(dummpy.val, end=',')
        dummpy = dummpy.next
    # 开始翻转链表
    res = reverseListNode(head)
    print("\nThis is reversed ListNodes: ")
    while res:
        print(res.val, end=',')
        res = res.next




