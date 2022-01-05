#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (53.11%)
# Likes:    5696
# Dislikes: 88
# Total Accepted:    266K
# Total Submissions: 500.2K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
# 
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were
# broken into on the same night.
# 
# Given the root of the binary tree, return the maximum amount of money the
# thief can rob without alerting the police.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def traverse(node: Optional[TreeNode]):
            if not node:
                return 0, 0
            leftrob, leftnotrob = traverse(node.left)
            rightrob, rightnotrob = traverse(node.right)
            rob = node.val + leftnotrob + rightnotrob
            notrob = max(leftrob, leftnotrob) + max(rightrob, rightnotrob)
            return rob, notrob
        
        return max(traverse(root))

# @lc code=end

