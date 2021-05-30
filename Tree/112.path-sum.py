#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
# @lc code=end


# bfs
'''
# @lc code=start
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            currentNode, currentSum = stack.pop(0)
            if not currentNode.left and not currentNode.right and currentSum == targetSum:
                return True
            if currentNode.left:
                stack.append((currentNode.left, currentSum + currentNode.left.val))
            if currentNode.right:
                stack.append((currentNode.right, currentSum + currentNode.right.val))
        return False
# @lc code=end
'''


# Test
testcase = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,1]

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

print(Solution().hasPathSum(root, 22))
print(root.right.right.right.val)