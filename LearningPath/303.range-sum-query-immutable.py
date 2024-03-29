#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (53.37%)
# Likes:    1685
# Dislikes: 1545
# Total Accepted:    317.5K
# Total Submissions: 594.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
#  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, handle multiple queries of the following
# type:
# 
# 
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
# 
# 
# Implement the NumArray class:
# 
# 
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
# 
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sumRange.
# 
# 
#


from typing import List


# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i+1] = self.sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right+1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end


# Test
testcase = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]

print(NumArray(testcase[0]).sumRange(testcase[1][0], testcase[1][1]))