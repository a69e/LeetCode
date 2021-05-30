#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for num in range(0, n):
            C = C * 2 * (2 * num + 1) / (num + 2)
        return int(C)
# @lc code=end


# Test
print(Solution().numTrees(5))