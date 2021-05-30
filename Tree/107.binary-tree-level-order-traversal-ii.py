#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        cur = [root]
        while cur:
            cur_val = []
            next_node = []
            for x in cur:
                cur_val.append(x.val)
                if x.left:
                    next_node.append(x.left)
                if x.right:
                    next_node.append(x.right)
            cur = next_node
            queue.insert(0, cur_val)
        return queue      
# @lc code=end


# Test
testcase = [3,9,20,None,None,15,7]

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

print(Solution().levelOrderBottom(root))