#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root: TreeNode, lst: List[int]):
            if not root:
                return
            if not root.left and not root.right:
                if sum(lst) + root.val == targetSum:
                    result.append([*lst, root.val])
                return
            dfs(root.left, [*lst, root.val])
            dfs(root.right, [*lst, root.val])
        dfs(root, [])
        return result
# @lc code=end


# Test
testcase = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]

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

print(Solution().pathSum(root, 22))