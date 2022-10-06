class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(head, node):
    """
    对于一个单链表head，删除它的其中一个节点node
    确保删除node后，之前的元素和之后的元素能串联，顺序不发生变化（node不能为最后一个节点值）
    如head=[4,5,1,9], node=1 -> head=[4,5,9]
    :param node: 单链表head和需要删除的链表节点值 [ListNode], [int]
    :return: 删除节点后的单链表 [ListNode]
    """
    resNode = head  # 使用另一条作为链表记录用于返回
    while head:
        if head.val == node:
            head.val = head.next.val
            head.next = head.next.next
        else:
            head = head.next

    return resNode


# 测试
if __name__ == "__main__":
    # 创建单链表
    head_test = ListNode(4)
    head_test.next = ListNode(5)
    head_test.next.next = ListNode(1)
    head_test.next.next.next = ListNode(9)
    # 记录链表值
    def recordValue(listNode):
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res

    head = head_test  # 复制链表
    ori_values = recordValue(head_test)
    print(f"输入的原始链表值为: {ori_values} .")

    node = 5  # 删除的节点值为5
    result = deleteNode(head, node)
    cal_values = recordValue(result)
    print(f"经过节点处理，现在的链表值为: {cal_values} .")