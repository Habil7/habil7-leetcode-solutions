class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_ways = 1
        curr_ways = 2

        for _ in range(2, n):
            prev_ways, curr_ways = curr_ways, prev_ways + curr_ways

        return curr_ways