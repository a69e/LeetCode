#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (61.73%)
# Likes:    3369
# Dislikes: 113
# Total Accepted:    453.3K
# Total Submissions: 732.2K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 1 <= k <= n
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(lst: List, i: int, k: int):
            if k == 0:
                ans.append(list(lst))
                return
            for num in range(i, n + 1):
                lst += [num]
                backtrack(lst, num + 1, k - 1)
                lst.pop()

        backtrack([], 1, k)
        return ans
        
# @lc code=end


# Test
print(Solution().combine(4,2))