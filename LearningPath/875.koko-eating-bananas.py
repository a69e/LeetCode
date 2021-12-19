#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (54.26%)
# Likes:    2394
# Dislikes: 129
# Total Accepted:    109.5K
# Total Submissions: 201.8K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time(k: int) -> int:
            return sum(int((p-1) / k) + 1 for p in piles)
        
        left, right = 1, 1000000001
        while (left < right):
            mid = int(left + (right - left) / 2)
            if time(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

        
# @lc code=end


# Test
testcase = [3,6,7,11]

print(Solution().minEatingSpeed(testcase, 8))