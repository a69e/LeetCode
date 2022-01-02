#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (60.88%)
# Likes:    1711
# Dislikes: 61
# Total Accepted:    56.7K
# Total Submissions: 92.9K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted
# characters to make two strings equal.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# Example 2:
# 
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        been = [[0] * len(s2) for _ in range(len(s1))]
        
        def dp(i: int, j: int):
            if i == len(s1):
                return sum([ord(s) for s in s2[j:]])
            if j == len(s2):
                return sum([ord(s) for s in s1[i:]])
            if been[i][j] != 0:
                return been[i][j]
            if s1[i] == s2[j]:
                been[i][j] = dp(i + 1, j + 1)
            else:
                been[i][j] = min(dp(i, j + 1) + ord(s2[j]), ord(s1[i]) + dp(i + 1, j))
            return been[i][j]
        
        return dp(0, 0)
        
# @lc code=end


# Test
testcase = 'sea'

print(Solution().minimumDeleteSum(testcase, 'eat'))