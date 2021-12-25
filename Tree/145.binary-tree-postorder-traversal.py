#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (61.88%)
# Likes:    3488
# Dislikes: 131
# Total Accepted:    615.6K
# Total Submissions: 993K
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iteration
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack, pre = [], [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right and root.right != pre:
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                pre = root
                root = None
        return ans

# @lc code=end


# Recursion
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def recurse(root: Optional[TreeNode]):
            if not root:
                return
            recurse(root.left)
            recurse(root.right)
            ans.append(root.val)

        recurse(root)
        return ans
'''