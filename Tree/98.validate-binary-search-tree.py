#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iteration
'''
# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        floor = float('-inf')
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= floor:
                return False
            floor = root.val
            root = root.right
        return True
# @lc code=end
'''


# recursion2 - question: how to exit right after return a False?
# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        floor = float('-inf')
        def dfs(root):
            nonlocal floor
            if root:
                dfs(root.left)
                if root.val <= floor:
                    return False
                floor = root.val
                dfs(root.right)
            return True
        return dfs(root)
# @lc code=end


# recursion
'''
# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, floor=float('-inf'), ceiling=float('inf')):
            if root:
                return floor<root.val<ceiling and dfs(root.left, floor, root.val) and dfs(root.right, root.val, ceiling)
            return True
        return dfs(root)
# @lc code=end
'''


# Test
testcase3 = [5,4,6,None,None,3,7]
testcase2 = [1,1]
testcase1 = [2,1,3]
testcase = [5,1,4,None,None,3,6]

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

print(Solution().isValidBST(root))