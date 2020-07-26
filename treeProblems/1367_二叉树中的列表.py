# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
#
# 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
#
# 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root: return False
        if dfs(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


def dfs(head, root):
    if not head: return True
    if not root: return False
    if root.val != head.val: return False
    if dfs(head.next, root.left) or dfs(head.next, root.right):
        return True

    return False