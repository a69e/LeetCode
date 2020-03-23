test_case = 'aadabc'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            sub_length = 0
            hash_list = [0 for _ in range(128)]
            for j in range(i, len(s)):
                if hash_list[ord(s[j])] == 0:
                    hash_list[ord(s[j])] = 1
                    sub_length += 1
                else:
                    break
            if sub_length > max_length:
                max_length = sub_length
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(test_case))
