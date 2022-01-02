#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.77%)
# Likes:    5158
# Dislikes: 60
# Total Accepted:    323.2K
# Total Submissions: 549.5K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# A common subsequence of two strings is a subsequence that is common to both
# strings.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        been = [[-1] * n for _ in range(m)]
        
        def dp(i: int, j: int):
            if i == m or j == n:
                return 0
            if been[i][j] != -1:
                return been[i][j]
            if text1[i] == text2[j]:
                been[i][j] = dp(i + 1, j + 1) + 1
            else:
                been[i][j] = max(dp(i, j + 1), dp(i + 1, j))
            return been[i][j]
        
        return dp(0, 0)

# @lc code=end


# Test
testcase = 'ylqpejqbalahwr'

print(Solution().longestCommonSubsequence(testcase, 'yrkzavgdmdgtqpg'))