#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
#
# algorithms
# Medium (47.79%)
# Likes:    526
# Dislikes: 107
# Total Accepted:    22.3K
# Total Submissions: 46.5K
# Testcase Example:  '"(()))"'
#
# Given a parentheses string s containing only the characters '(' and ')'. A
# parentheses string is balanced if:
# 
# 
# Any left parenthesis '(' must have a corresponding two consecutive right
# parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right
# parenthesis '))'.
# 
# 
# In other words, we treat '(' as an opening parenthesis and '))' as a closing
# parenthesis.
# 
# 
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))"
# and "(()))" are not balanced.
# 
# 
# You can insert the characters '(' and ')' at any position of the string to
# balance it if needed.
# 
# Return the minimum number of insertions needed to make s balanced.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only
# ')' matching. We need to to add one more ')' at the end of the string to be
# "(())))" which is balanced.
# 
# 
# Example 2:
# 
# 
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# 
# 
# Example 3:
# 
# 
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last
# '('.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of '(' and ')' only.
# 
# 
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        used, need = 0, 0
        for i in s:
            if i == '(':
                need += 2
                if need % 2 == 1:
                    used += 1
                    need -= 1
            else:
                if need > 0:
                    need -= 1
                else:
                    used += 1
                    need += 1
        return used + need
        
# @lc code=end


# Test
testcase = '))(()()))()))))))()())()(())()))))()())(()())))()('

print(Solution().minInsertions(testcase))