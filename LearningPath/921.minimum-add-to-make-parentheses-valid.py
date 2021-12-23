#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (77.48%)
# Likes:    1930
# Dislikes: 107
# Total Accepted:    157.8K
# Total Submissions: 203.6K
# Testcase Example:  '"())"'
#
# A parentheses string is valid if and only if:
# 
# 
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# You are given a parentheses string s. In one move, you can insert a
# parenthesis at any position of the string.
# 
# 
# For example, if s = "()))", you can insert an opening parenthesis to be
# "(()))" or a closing parenthesis to be "())))".
# 
# 
# Return the minimum number of moves required to make s valid.
# 
# 
# Example 1:
# 
# 
# Input: s = "())"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: s = "((("
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "()"
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: s = "()))(("
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
# 
# 
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1 
            elif left >0:
                left -= 1
            else:
                right += 1
        return left + right
            
        
# @lc code=end

