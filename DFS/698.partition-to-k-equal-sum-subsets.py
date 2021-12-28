#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (45.93%)
# Likes:    4178
# Dislikes: 244
# Total Accepted:    175.8K
# Total Submissions: 382.6K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an integer array nums and an integer k, return true if it is possible
# to divide this array into k non-empty subsets whose sums are all equal.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.count = 0
        target = sum(nums) / k
        if not target.is_integer():
            return False
        sums = [0] * k

        def backtrack(nums: List[int], index):
            if index == len(nums):
                if len(set(sums)) == 1:
                    return True
                return False
            for i in range(k):
                sums[i] += nums[index]
                if sums[i] > target:
                    sums[i] -= nums[index]
                    continue
                if backtrack(nums, index+1):
                    return True
                sums[i] -= nums[index]
            return False

        return backtrack(sorted(nums, reverse=True), 0)
        
# @lc code=end


# Test
testcase = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]

print(Solution().canPartitionKSubsets(testcase,5))