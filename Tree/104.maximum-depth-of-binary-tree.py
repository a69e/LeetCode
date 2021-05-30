#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0
        
# @lc code=end


# Test
testcase = [1,2,3,3,4,4,5,6]

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

print(Solution().maxDepth(root))