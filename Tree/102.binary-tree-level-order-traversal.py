#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = [root]
        while queue:
            tempQueue = queue
            queue = []
            tempNodeValueList = []
            while tempQueue:
                tempTreeNode = tempQueue.pop(0)
                tempNodeValueList.append(tempTreeNode.val)
                if tempTreeNode.left:
                    queue.append(tempTreeNode.left)
                if tempTreeNode.right:
                    queue.append(tempTreeNode.right)
            output.append(tempNodeValueList)
        return output
# @lc code=end


# Test
testcase = [1,2,2,3,4,4,3]

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

print(Solution().levelOrder(root))