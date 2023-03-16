"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""

"""
使用分治法+递归法，先无限将链表列表二分，直到只有1个链表为止
然后每次对划分的左、右列表进行合并，即两个升序链表的合并：
（1）判断当前l1和l2是否不为空，如果为空返回另一个链表（意味后续值直接添加）
（2）当l1.val <= l2.val，保留l1的元素，且l1.next应该等于l1.next和l2链表合并的结果，最后返回l1
同样，如果l1.val > l2.val，保留l2的元素，且l2.next应该等于l2.next和l1链表合并的结果，最后返回l2
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        n = len(lists)
        if n == 1:
            return lists[0]
        else:
            mid = n // 2
            left = self.mergeKLists(lists[: mid])
            right = self.mergeKLists((lists[mid: ]))

            return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
