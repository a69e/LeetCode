#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (70.40%)
# Likes:    8392
# Dislikes: 166
# Total Accepted:    1M
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrack(nums: List[int], ans: List[int]):
            if not nums:
                self.ans.append(ans)
                return
            for i, num in enumerate(nums):
                backtrack(nums[:i]+nums[i+1:], ans+[num])

        backtrack(nums, [])
        return self.ans
        
# @lc code=end


# Test
testcase = [1,2]

print(Solution().permute(testcase))