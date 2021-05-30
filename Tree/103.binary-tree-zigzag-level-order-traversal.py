#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#


from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = [root]
        flag = True
        while queue:
            tempQueue = queue
            queue = []
            tempNodeValueList = deque([])
            while tempQueue:
                tempTreeNode = tempQueue.pop(0)
                if flag:
                    tempNodeValueList.append(tempTreeNode.val)
                else:
                    tempNodeValueList.appendleft(tempTreeNode.val)
                if tempTreeNode.left:
                    queue.append(tempTreeNode.left)
                if tempTreeNode.right:
                    queue.append(tempTreeNode.right)
            output.append(list(tempNodeValueList))
            flag = not flag
        return output
# @lc code=end


# Test
testcase = [1,2,3,3,4,4,5]

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

print(Solution().zigzagLevelOrder(root))