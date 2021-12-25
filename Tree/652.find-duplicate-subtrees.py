#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (55.00%)
# Likes:    2746
# Dislikes: 275
# Total Accepted:    126.6K
# Total Submissions: 230K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200
# 
# 
#


from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans, hash = [], {}
        
        def recurse(node: Optional[TreeNode]):
            if not node:
                return '*'
            left = recurse(node.left)
            right = recurse(node.right)
            subtree = left + '-' + right + '-' + str(node.val)
            hash[subtree] = hash.get(subtree, 0) + 1
            if hash[subtree] == 2:
                ans.append(node)
            return subtree
        
        recurse(root)
        return ans

# @lc code=end


# Test
testcase = [0,0,0,0,None,None,0,None,None,None,0]

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

print(Solution().findDuplicateSubtrees(root))