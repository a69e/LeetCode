#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# @lc code=start
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def connect2nodes(node1: 'Node', node2: 'Node'):
            if not node1 or not node2:
                return
            node1.next = node2
            connect2nodes(node1.left, node1.right)
            connect2nodes(node1.right, node2.left)
            connect2nodes(node2.left, node2.right)
        
        if not root:
            return None
        connect2nodes(root.left, root.right)
        return root
        
# @lc code=end


# Iteration
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        leftMost = root
        while leftMost.left:
            head = leftMost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftMost = leftMost.left
        return root
'''


# Test
testcase = [1,2,3,4,5,6,7]

def genTreeNode(treenode, lst, index):
    if index < len(lst):
        if lst[index] is None:
            return None
        else:
            treenode = Node(lst[index])
            treenode.left = genTreeNode(treenode.left, lst, 2 * index + 1)
            treenode.right = genTreeNode(treenode.right, lst, 2 * index + 2)
            return treenode
    return treenode
root = genTreeNode(Node(), testcase, 0)

print(Solution().connect(root).left.right.next.val)