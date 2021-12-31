#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (67.84%)
# Likes:    2512
# Dislikes: 246
# Total Accepted:    592.4K
# Total Submissions: 873.3K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
# 
# 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# 
# 
# Given n, calculate F(n).
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 30
# 
# 
#


# Iteration
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        prepre, pre = 0, 1
        for i in range(2, n + 1):
            cur = prepre + pre
            prepre = pre
            pre = cur
        return cur

# @lc code=end


# Recursion
'''
class Solution:
    def fib(self, n: int) -> int:
        been = [0] * n

        def recurse(n: int):
            if n == 0 or n == 1:
                return n
            if not been[n - 1]:
                been[n - 1] = recurse(n - 1)
            if not been[n - 2]:
                been[n - 2] = recurse(n - 2)
            return been[n - 1] + been[n - 2]
        
        return recurse(n)
'''    


# Test
testcase = 5

print(Solution().fib(testcase))