'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None

        while head:
            head.next, p, head = p, head, head.next

        return p



l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

s = Solution()
s.reverseList(l)