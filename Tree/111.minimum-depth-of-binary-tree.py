#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
# @lc code=start
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        while stack:
            temp, depth = stack.pop(0)
            if not temp.left and not temp.right:
                return depth
            if temp.left:
                stack.append((temp.left, depth + 1))
            if temp.right:
                stack.append((temp.right, depth + 1))
# @lc code=end


# dfs
'''
# @lc code=start
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        result = float('inf')
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left:
            result = min(self.minDepth(root.left) + 1, result)
        if root.right:
            result = min(self.minDepth(root.right) + 1, result)
        return result
# @lc code=end
'''


# Test
testcase = [3,9,20,None,None,15,7]

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

print(Solution().minDepth(root))