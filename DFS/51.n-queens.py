#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (55.13%)
# Likes:    4654
# Dislikes: 137
# Total Accepted:    322.7K
# Total Submissions: 584K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [["Q"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.' * n for _ in range(n)]
        ans = []

        def backtrack(board, row):
            if row == n:
                ans.append(list(board))
                return
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                temp = list(board[row])
                temp[col] = 'Q'
                board[row] = ''.join(temp)
                backtrack(board, row + 1)
                board[row] = '.' * n
        
        def isValid(board, row, col):
            for r in range(n):
                if board[r][col] == 'Q':
                    return False
            r, c = row, col
            while r > 0 and c > 0:
                if board[r-1][c-1] == 'Q':
                    return False
                r -= 1
                c -= 1
            r, c = row, col
            while r > 0 and c < n - 1:
                if board[r-1][c+1] == 'Q':
                    return False
                r -= 1
                c += 1
            return True

        backtrack(board, 0)
        return ans
        
# @lc code=end


# Test
print(Solution().solveNQueens(4))