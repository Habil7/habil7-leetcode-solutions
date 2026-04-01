class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n

        current = n
        for i, ch in enumerate(s):
            if ch == c:
                current = 0
            else:
                current += 1
            ans[i] = current

        current = n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                current = 0
            else:
                current += 1
            ans[i] = min(ans[i], current)
        return ans
