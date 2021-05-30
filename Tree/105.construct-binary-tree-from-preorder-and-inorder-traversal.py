#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hashMap = {element: i for i, element in enumerate(inorder)}
        def dfs(preorder: List[int], inorder: List[int]):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            leftTreeLen = hashMap[preorder[0]] - hashMap[inorder[0]]
            root.left = dfs(preorder[1:leftTreeLen+1], inorder[:leftTreeLen])
            root.right = dfs(preorder[leftTreeLen+1:], inorder[leftTreeLen+1:])
            return root
        return dfs(preorder, inorder)
# @lc code=end


# Test
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(Solution().buildTree(preorder, inorder).right.right.val)