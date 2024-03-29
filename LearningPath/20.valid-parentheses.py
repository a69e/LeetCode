#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.56%)
# Likes:    10260
# Dislikes: 403
# Total Accepted:    1.8M
# Total Submissions: 4.5M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif not stack or i != pair[stack.pop()]:
                return False
        return True if not stack else False
        
# @lc code=end


# Test
testcase = '()[]{}'

print(Solution().isValid(testcase))