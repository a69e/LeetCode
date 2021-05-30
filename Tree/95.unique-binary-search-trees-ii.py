#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None]
            treeList = []
            for i in range(start, end + 1):
                leftTrees = generateTrees(start, i - 1)
                rightTrees = generateTrees(i + 1, end)
            
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        tempTree = TreeNode(i)
                        tempTree.left = leftTree
                        tempTree.right = rightTree
                        treeList.append(tempTree)
            return treeList
        return generateTrees(1, n) if n else []
# @lc code=end


# Test
print(Solution().generateTrees(2)[0])