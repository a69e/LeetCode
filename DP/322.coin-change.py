#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (39.24%)
# Likes:    9370
# Dislikes: 228
# Total Accepted:    834.9K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#


from typing import List


# Iteration
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
# @lc code=end


# Recursion
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        been = {}

        def dp(coins: List[int], amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            ans = float('inf')
            for coin in coins:
                if amount in been:
                    return been[amount]
                temp = dp(coins, amount - coin)
                if temp == -1:
                    continue
                ans = min(temp + 1, ans)
            been[amount] = ans if ans != float('inf') else -1
            return been[amount]

        return dp(coins, amount)
'''


# Time limit exceeded
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        been = {coin: 1 for coin in coins}
        for _ in range(int(amount / min(coins)) + 1):
            temp = dict(been)
            for num in temp:
                if num == amount:
                    return been[num]
                for coin in coins:
                    if num + coin in been:
                        continue
                    else:
                        been[num + coin] = been[num] + 1
        return been[amount] if amount in been else -1
'''


# Test
testcase = [1,2,5]
testcase2 = [3,7,405,436]
testcase3 = [2,4,6,8,10,12,14,16,18,20,22,24]

print(Solution().coinChange(testcase, 11))
print(Solution().coinChange(testcase2, 8839))
print(Solution().coinChange(testcase3, 9999))