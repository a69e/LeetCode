#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (68.96%)
# Likes:    7809
# Dislikes: 129
# Total Accepted:    926.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        temp = self.subsets(nums[1:])
        return [ num + [nums[0]] for num in temp] + temp

# @lc code=end


# Test
testcase = [1,3,2]

print(Solution().subsets(testcase))