#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
# https://leetcode.com/problems/stone-game-ii/description/
#
# algorithms
# Medium (64.69%)
# Likes:    1145
# Dislikes: 237
# Total Accepted:    35.7K
# Total Submissions: 55.2K
# Testcase Example:  '[2,7,9,4,4]'
#
# Alice and Bob continue their games with piles of stones.  There are a number
# of piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].  The objective of the game is to end with the most stones. 
# 
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
# 
# On each player's turn, that player can take all the stones in the first X
# remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# 
# The game continues until all the stones have been taken.
# 
# Assuming Alice and Bob play optimally, return the maximum number of stones
# Alice can get.
# 
# 
# Example 1:
# 
# 
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles,
# then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total.
# If Alice takes two piles at the beginning, then Bob can take all three piles
# left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since
# it's larger. 
# 
# 
# Example 2:
# 
# 
# Input: piles = [1,2,3,4,5,100]
# Output: 104
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10^4
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        sums = 0
        dp = [[0 for j in range(l)] for i in range(l)]
        for i in range(l - 1, -1, -1):
            sums += piles[i]
            for j in range(int(l / 2) + 1):
                if i + 2 * (j + 1) >= l:
                    dp[i][j] = sums
                else:
                    for k in range(1, 2 * (j + 1) + 1):
                        dp[i][j] = max(dp[i][j], sums - dp[i + k][max(j, k - 1)])
        return dp[0][0]
        
# @lc code=end


# Test
testcase = [1]

print(Solution().stoneGameII(testcase))