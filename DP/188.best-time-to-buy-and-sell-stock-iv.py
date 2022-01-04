#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (32.23%)
# Likes:    3370
# Dislikes: 150
# Total Accepted:    219.6K
# Total Submissions: 676.8K
# Testcase Example:  '2\n[2,4,1]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day, and an integer k.
# 
# Find the maximum profit you can achieve. You may complete at most k
# transactions.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit
# = 3-0 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0, float('-inf')] for _ in range(k + 1)]
        for i in range(len(prices)):
            for j in range(1, k + 1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                if j == 1:
                    dp[j][1] = max(dp[j][1], -prices[i])
                else:
                    dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
        return dp[k][0]
        
# @lc code=end


# Test
testcase = [7,1,5,3,6,4]

print(Solution().maxProfit(2, testcase))