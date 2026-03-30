class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        longest_length = 0
        n = len(s)

        for center in range(n):
            left = center
            right = center

            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > longest_length:
                    longest_substring = s[left:right + 1]
                    longest_length = current_length

                left -= 1
                right += 1

            left = center
            right = center + 1

            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > longest_length:
                    longest_substring = s[left:right + 1]
                    longest_length = current_length

                left -= 1
                right += 1

        return longest_substring
