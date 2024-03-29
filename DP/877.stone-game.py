#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (68.73%)
# Likes:    1754
# Dislikes: 1857
# Total Accepted:    142.5K
# Total Submissions: 207.1K
# Testcase Example:  '[5,3,4,5]'
#
# Alice and Bob play a game with piles of stones. There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
# 
# The objective of the game is to end with the most stones. The total number of
# stones across all the piles is odd, so there are no ties.
# 
# Alice and Bob take turns, with Alice starting first. Each turn, a player
# takes the entire pile of stones either from the beginning or from the end of
# the row. This continues until there are no more piles left, at which point
# the person with the most stones wins.
# 
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or
# false if Bob wins.
# 
# 
# Example 1:
# 
# 
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10
# points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we
# return true.
# 
# 
# Example 2:
# 
# 
# Input: piles = [3,7,2,3]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[(piles[i], 0) if i == j else (0, 0) for j in range(l)] for i in range(l)]
        for i in range(l - 2, -1, -1):
            for j in range(i + 1, l):
                left = piles[i] + dp[i + 1][j][1]
                right = dp[i][j - 1][1] + piles[j]
                if left > right:
                    dp[i][j] = (left, dp[i + 1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j - 1][0])
        return dp[0][l - 1][0] > dp[0][l - 1][1]
        
# @lc code=end


# Test
testcase = [5,3,4,5]

print(Solution().stoneGame(testcase))