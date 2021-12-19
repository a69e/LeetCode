#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.15%)
# Likes:    8370
# Dislikes: 258
# Total Accepted:    915.1K
# Total Submissions: 2.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, ans = 0, len(nums), []
        while (left < right):
            mid = int(left + (right - left) / 2)
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        ans.append(left)
        left, right = 0, len(nums)
        while (left < right):
            mid = int(left + (right - left) / 2)
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        ans.append(right-1)
        return ans if ans[0] <= ans[1] else [-1, -1]
            
        
# @lc code=end


# Test
testcase = [5,7,7,8,8,10]

print(Solution().searchRange(testcase, 6))