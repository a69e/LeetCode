#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
# https://leetcode.com/problems/open-the-lock/description/
#
# algorithms
# Medium (55.12%)
# Likes:    2433
# Dislikes: 85
# Total Accepted:    141K
# Total Submissions: 255.7K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.
# 
# The lock initially starts at '0000', a string representing the state of the 4
# wheels.
# 
# You are given a list of deadends dead ends, meaning if the lock displays any
# of these codes, the wheels of the lock will stop turning and you will be
# unable to open it.
# 
# Given a target representing the value of the wheels that will unlock the
# lock, return the minimum total number of turns required to open the lock, or
# -1 if it is impossible.
# 
# 
# Example 1:
# 
# 
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
# "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
# would be invalid,
# because the wheels of the lock become stuck after the display becomes the
# dead end "0102".
# 
# 
# Example 2:
# 
# 
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" ->
# "0009".
# 
# 
# Example 3:
# 
# 
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
# 
# 
#


from typing import List
from collections import deque


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        used = set(deadends)
        stack = deque([('0000', 0)])

        def up(s: str, index: int):
            temp = list(s)
            temp[index] = '0' if temp[index] == '9' else str(int(temp[index]) + 1)
            return ''.join(temp)

        def down(s: str, index: int):
            temp = list(s)
            temp[index] = '9' if temp[index] == '0' else str(int(temp[index]) - 1)
            return ''.join(temp)

        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        while stack:
            num, count = stack.popleft()
            for i in range(4):
                for move in ('up', 'down'):
                    temp = up(num, i) if move == 'up' else down(num, i)
                    if temp not in used:
                        if temp == target:
                            return count + 1
                        used.add(temp)
                        stack.append((temp, count + 1))
        return -1
        
# @lc code=end


# Test
testcase = ["8887","8889","8878","8898","8788","8988","7888","9888"]

print(Solution().openLock(testcase, '8888'))