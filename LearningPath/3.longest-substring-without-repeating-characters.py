#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.56%)
# Likes:    19557
# Dislikes: 891
# Total Accepted:    2.8M
# Total Submissions: 8.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window, left, right, ans = {}, 0, 0, 0
        while (right < len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if window[s[right]] == 1 and len(window) > ans:
                ans = len(window)
            right += 1
            while (window[s[right-1]] > 1):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
        return ans

        
# @lc code=end

# Test
testcase = 'abcabcbb'

print(Solution().lengthOfLongestSubstring(testcase))