#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        wrong1, wrong2, pointer = None, None, None
        def dfs(root):
            nonlocal wrong1, wrong2, pointer
            if root:
                dfs(root.left)
                if not pointer:
                    pointer = root
                else:
                    if pointer.val >= root.val:
                        wrong2 = root
                        if not wrong1:
                            wrong1 = pointer
                    pointer = root
                dfs(root.right)
        dfs(root)
        wrong1.val, wrong2.val = wrong2.val, wrong1.val
# @lc code=end


# Test
testcase1 = [1,None,3,None,None,None,2]
testcase = [3,1,4,None,None,2]

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
root = genTreeNode(TreeNode(), testcase1, 0)

Solution().recoverTree(root)
print(root.right.val)