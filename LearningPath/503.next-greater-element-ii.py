#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (60.94%)
# Likes:    3700
# Dislikes: 119
# Total Accepted:    184K
# Total Submissions: 301.8K
# Testcase Example:  '[1,2,1]'
#
# Given a circular integer array nums (i.e., the next element of
# nums[nums.length - 1] is nums[0]), return the next greater number for every
# element in nums.
# 
# The next greater number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, return -1 for this
# number.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also
# 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stack, temp = [-1 for _ in range(len(nums)*2)], [], list(reversed(nums*2))
        for i in range(len(nums)*2):
            while stack and stack[-1] <= temp[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(temp[i])
        return list(reversed(res))[:len(nums)]


# @lc code=end


# Test
testcase = [1,2,3,4,3]

print(Solution().nextGreaterElements([1,2,1]))