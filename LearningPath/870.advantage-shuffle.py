#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#
# https://leetcode.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (51.00%)
# Likes:    1151
# Dislikes: 72
# Total Accepted:    50.1K
# Total Submissions: 98.3K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# You are given two integer arrays nums1 and nums2 both of the same length. The
# advantage of nums1 with respect to nums2 is the number of indices i for which
# nums1[i] > nums2[i].
# 
# Return any permutation of nums1 that maximizes its advantage with respect to
# nums2.
# 
# 
# Example 1:
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        win = {num: [] for num in nums2}
        lose = []
        nums1.sort(reverse=True)
        sorted2 = sorted(nums2, reverse=True)
        while nums1:
            num = nums1.pop()
            if num > sorted2[-1]:
                win[sorted2.pop()].append(num)
            else:
                lose.append(num)
        return [win[num].pop() if win[num] else lose.pop() for num in nums2]
        
# @lc code=end


# Test
testcase = [2,0,4,1,2]

print(Solution().advantageCount(testcase, [1,3,0,0,2]))