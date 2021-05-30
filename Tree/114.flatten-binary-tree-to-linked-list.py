#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
# @lc code=start
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            leftTree = root.left
            rightTree = root.right
            root.left = None
            root.right = leftTree
            temp = root
            while temp.right:
                temp = temp.right
            temp.right = rightTree
# @lc code=end


# Morris
'''
# @lc code=start
class Solution:
    def flatten(self, root: TreeNode) -> None:
        current = root
        while current:
            if current.left:
                pre = current.left
                while pre.right:
                    pre = pre.right
                pre.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
# @lc code=end
'''


# Test
testcase = [1,2,5,3,4,None,6]

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

print(Solution().flatten(root))