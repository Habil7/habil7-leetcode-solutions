class Solution:
    def minOperations(self, lst: List[int], k: int) -> int:
        count = 0 

        for num in lst:
            count += num

        return count % k