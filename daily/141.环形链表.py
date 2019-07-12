'''
给定一个链表，判断链表中是否有环。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# python特性解法
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head:
            if head in s:
                return True
            else:
                s.add(head)
            head = head.next
        return False

# 快慢指针
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast,low = head,head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
            if fast is low:
                return True
        return False