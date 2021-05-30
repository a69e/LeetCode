#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Morris
# @lc code=start
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        while root:
            if root.left:
                father = root.left
                while father.right and father.right != root:
                    father = father.right
                if father.right:
                    output.append(root.val)
                    root = root.right
                else:
                    father.right = root
                    root = root.left
            else:
                output.append(root.val)
                root = root.right
        return output
# @lc code=end


# Iteration
'''
# @lc code=start
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []
        while (root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        return output
# @lc code=end
'''


# Recursion
'''
# @lc code=start
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        def dfs(root: TreeNode):
            if root:
                dfs(root.left)
                output.append(root.val)
                dfs(root.right)
        dfs(root)
        return output
# @lc code=end
'''


# Test
testcase = [1,None,2,None,None,3]

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

print(Solution().inorderTraversal(root))