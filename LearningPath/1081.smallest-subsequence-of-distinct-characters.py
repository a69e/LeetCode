#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (54.62%)
# Likes:    1295
# Dislikes: 133
# Total Accepted:    30.8K
# Total Submissions: 56.4K
# Testcase Example:  '"bcabc"'
#
# Given a string s, return the lexicographically smallest subsequence of s that
# contains all the distinct characters of s exactly once.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count, stack = collections.Counter(s), []
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return ''.join(stack)
        
# @lc code=end

