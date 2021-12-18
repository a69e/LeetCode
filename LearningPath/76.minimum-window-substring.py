#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.12%)
# Likes:    8810
# Dislikes: 501
# Total Accepted:    661K
# Total Submissions: 1.7M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, window, left, right, match, ans = {}, {}, 0, 0, 0, ''
        for i in t:
            target[i] = target.get(i, 0) + 1
        while (right < len(s)):
            if s[right] in target:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == target[s[right]]:
                    match += 1
            right += 1
            while (match == len(target)):
                if not ans or len(ans) > right - left:
                    ans = s[left:right]
                if s[left] in window:
                    if window[s[left]] == target[s[left]]:
                        match -= 1
                    window[s[left]] -= 1
                left += 1
        return ans


# @lc code=end


# Test
testcase = 'ADOBECODEBANC'

print(Solution().minWindow(testcase, 'ABC'))