class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen_chars = set()
        n = len(s)

        for right in range(n):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            seen_chars.add(s[right])
            window_length = (right - left) + 1
            longest = max(longest, window_length)

        return longest