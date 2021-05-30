#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hashMap = {element: i for i, element in enumerate(inorder)}
        def dfs(inorder: List[int], postorder: List[int]):
            if not postorder:
                return None
            root = TreeNode(postorder[-1])
            leftTreeLen = hashMap[postorder[-1]] - hashMap[inorder[0]]
            root.left = dfs(inorder[:leftTreeLen], postorder[:leftTreeLen])
            root.right = dfs(inorder[leftTreeLen+1:], postorder[leftTreeLen:-1])
            return root
        return dfs(inorder, postorder)
# @lc code=end


# Test
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

print(Solution().buildTree(inorder, postorder).right.right.val)