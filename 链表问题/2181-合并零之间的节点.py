# 定义链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 记录链表值
def recordValue(listNode):
    res = []
    while listNode:
        res.append(listNode.val)
        listNode = listNode.next
    return res


def mergeNodes(head):
    """
    给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。
    链表的 开端 和 末尾 的节点都满足 Node.val == 0
    对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。
    然后将所有 0 移除，修改后的链表不应该含有任何 0
    返回修改后链表的头节点 head
    :param head: 输入待修改的链表头节点head [ListNode]
    :return: 返回修改后的链表头 [ListNode]
    """
    # 创建另外2个链表，一个记录当前节点（指针变化），一个为返回节点（指针在头部）
    resNode = currNode = head
    # 遍历head
    while head:
        # 当此时节点值不等于0时，需要进行积累
        if head.val != 0:
            tmp = 0
            while head and head.val != 0:
                tmp += head.val
                head = head.next
            currNode.next = ListNode(tmp)
            currNode = currNode.next
        else:
            head = head.next

    # 最后需要注意，返回的不是头部节点，而是第二个节点位置
    return resNode.next


# 测试
if __name__ == "__main__":
    # 创建单链表: head = [0,1,0,3,0,2,2,0]
    head_test = ListNode(0)
    head_test.next = ListNode(1)
    head_test.next.next = ListNode(0)
    head_test.next.next.next = ListNode(3)
    head_test.next.next.next.next = ListNode(0)
    head_test.next.next.next.next.next = ListNode(2)
    head_test.next.next.next.next.next.next = ListNode(2)
    head_test.next.next.next.next.next.next.next = ListNode(0)
    # 初始链表
    head = head_test
    ori_values = recordValue(head_test)
    print(f"输入的原始链表值为: {ori_values} .")
    # 处理后的链表
    result = mergeNodes(head)
    cal_values = recordValue(result)
    print(f"经过节点处理，现在的链表值为: {cal_values} .")
