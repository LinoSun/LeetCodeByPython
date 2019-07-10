'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归算，不是最优解，但是更易懂，要回头看
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 迭代法，节省空间，但是代码多
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2

        tmp = ListNode(0)
        res = tmp
        # 两个判断之后说明l1,l2都不为空
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        # l1或者l2出现空
        tmp.next = l1 if l2 is None else l2

        return res.next

# 尾递归法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        rootNode = ListNode(0)
        node = rootNode
        while l1 != None or l2 != None :
            if l1 == None :
                node.next = l2
                break
            if l2 == None :
                node.next = l1
                break
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else :
                node.next = l2
                l2 = l2.next
            node = node.next
        return rootNode.next