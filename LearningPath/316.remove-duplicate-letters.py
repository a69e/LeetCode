#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (40.84%)
# Likes:    3574
# Dislikes: 255
# Total Accepted:    145.2K
# Total Submissions: 355.3K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
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
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, stack = collections.Counter(s), []
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return ''.join(stack)
        
# @lc code=end
