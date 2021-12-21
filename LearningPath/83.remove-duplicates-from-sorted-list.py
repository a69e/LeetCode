#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (48.10%)
# Likes:    3784
# Dislikes: 172
# Total Accepted:    734.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,1,2]
# Output: [1,2]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer and pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next if pointer.next.next else None
            else:
                pointer = pointer.next
        return head
        
# @lc code=end

