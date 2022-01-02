#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (49.55%)
# Likes:    7322
# Dislikes: 86
# Total Accepted:    425.4K
# Total Submissions: 856K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        been = [[0] * len(word2) for _ in range(len(word1))]

        def dp(i: int, j: int):
            if i == len(word1):
                return len(word2[j:])
            if j == len(word2):
                return len(word1[i:])
            if been[i][j] != 0:
                return been[i][j]
            if word1[i] == word2[j]:
                been[i][j] = dp(i + 1, j + 1)
            else:
                been[i][j] = min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1)) + 1
            return been[i][j]
        
        return dp(0, 0)

# @lc code=end


# Test
testcase = 'horse'

print(Solution().minDistance(testcase, 'ros'))