#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.22%)
# Likes:    3828
# Dislikes: 101
# Total Accepted:    262.4K
# Total Submissions: 593.6K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, target, left, right = {}, {}, 0, 0
        if s1 == '':
            return True
        for i in s1:
            target[i] = target.get(i, 0) + 1
        while (right < len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if window == target:
                return True
            right += 1
            while (right - left == len(s1)):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])
                left += 1
        return False

        
# @lc code=end


# Test
testcase = 'ab'

print(Solution().checkInclusion(testcase, 'eidbaooo'))