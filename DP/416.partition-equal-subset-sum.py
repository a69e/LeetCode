#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.02%)
# Likes:    6502
# Dislikes: 107
# Total Accepted:    385.6K
# Total Submissions: 836.7K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if not target.is_integer():
            return False
        dp = [True] + [False] * int(target)
        for num in nums:
            for i in range(int(target), 0, -1):
                if i - num >= 0:
                    dp[i] = dp[i] or dp[i - num]
        return dp[int(target)]
        
# @lc code=end


# Test
testcase = [1,2,5]

print(Solution().canPartition(testcase))