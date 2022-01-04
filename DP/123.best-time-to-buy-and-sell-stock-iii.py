#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (42.35%)
# Likes:    5088
# Dislikes: 110
# Total Accepted:    351.4K
# Total Submissions: 827.7K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
# 
# 
# Example 3:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, float('-inf')], [0, float('-inf')]]
        for i in range(len(prices)):
            for j in (0, 1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                if j == 1:
                    dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                else:
                    dp[j][1] = max(dp[j][1], -prices[i])
        return dp[1][0]
        
# @lc code=end


# Test
testcase = [7,1,5,3,6,4]

print(Solution().maxProfit(testcase))