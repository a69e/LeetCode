#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (51.07%)
# Likes:    5050
# Dislikes: 173
# Total Accepted:    247.3K
# Total Submissions: 482.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
# 
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Example 2:
# 
# 
# Input: prices = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0, float('-inf'), 0]
        for i in range(len(prices)):
            temp = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[2] - prices[i])
            dp[2] = temp
        return dp[0]
        
# @lc code=end


# Test
testcase = [1,2,3,0,2]

print(Solution().maxProfit(testcase))