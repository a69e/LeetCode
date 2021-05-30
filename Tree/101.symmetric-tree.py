#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

# recursion
# @lc code=start
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetric(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return isSymmetric(p.left, q.right) and isSymmetric(p.right, q.left)
        return isSymmetric(root, root)
# @lc code=end


# bfs
'''
# @lc code=start
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        left = collections.deque([root.left])
        right = collections.deque([root.right])
        while left and right:
            currentLeft = left.popleft()
            currentRight = right.popleft()
            if currentLeft.val != currentRight.val:
                return False
            if not currentLeft.left and not currentRight.right:
                pass
            elif not currentLeft.left or not currentRight.right:
                return False
            else:
                left.append(currentLeft.left)
                right.append(currentRight.right)
            if not currentLeft.right and not currentRight.left:
                pass
            elif not currentLeft.right or not currentRight.left:
                return False
            else:
                left.append(currentLeft.right)
                right.append(currentRight.left)
        return not left and not right
# @lc code=end
'''


# Test
testcase1 = [1,2,2,None,3,None,3]
testcase = [1,2,2,3,4,4,3]

def genTreeNode(treenode, lst, index):
    if index < len(lst):
        if lst[index] is None:
            return None
        else:
            treenode = TreeNode(lst[index])
            treenode.left = genTreeNode(treenode.left, lst, 2 * index + 1)
            treenode.right = genTreeNode(treenode.right, lst, 2 * index + 2)
            return treenode
    return treenode
root = genTreeNode(TreeNode(), testcase, 0)

print(Solution().isSymmetric(root))