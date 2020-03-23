test_case = 'aadabc'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        prefix = 0
        hash_list = [-1 for _ in range(128)]
        for suffix in range(len(s)):
            prefix = max(prefix, hash_list[ord(s[suffix])] + 1)
            max_length = max(max_length, suffix - prefix + 1)
            hash_list[ord(s[suffix])] = suffix
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(test_case))
