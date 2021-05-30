#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum = 0

        def dfs(root: TreeNode) -> TreeNode:
            nonlocal sum
            if root:
                dfs(root.right)
                sum += root.val
                root.val= sum
                dfs(root.left)
        
        dfs(root)

        return root
# @lc code=end


# Test
testcase = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]

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

print(Solution().convertBST(root).left.right.right.val)