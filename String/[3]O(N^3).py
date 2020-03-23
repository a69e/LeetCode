test_case = 'aadabc'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string = ''
        for i in range(len(s)):
            substring = []
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring.append(s[j])
                else:
                    break
            if len(substring) > len(max_string):
                max_string = substring
        return len(max_string)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(test_case))
