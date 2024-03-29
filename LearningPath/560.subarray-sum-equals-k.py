#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.78%)
# Likes:    10104
# Dislikes: 333
# Total Accepted:    627.8K
# Total Submissions: 1.4M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        hash = {0:1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans += hash.get(sum - k, 0)
            hash[sum] = hash.get(sum, 0) + 1
        return ans
        

# @lc code=end


# Test
testcase = [1,2,3]

print(Solution().subarraySum(testcase, 3))