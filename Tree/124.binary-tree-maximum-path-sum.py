#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = root.val
        def dfs(node: TreeNode):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            side_max = max(left, right)
            self.ans = max(self.ans, (max(0, side_max, left + right) + node.val))
            return max(0, side_max) + node.val
        dfs(root)
        return self.ans        
# @lc code=end


# Test
testcase = [1,2,3,4,5,None,7]

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

print(Solution().maxPathSum(root))