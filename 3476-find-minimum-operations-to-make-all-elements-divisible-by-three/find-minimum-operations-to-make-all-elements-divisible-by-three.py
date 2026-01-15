class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operation = 0

        for num in nums:
            if num % 3 == 0:
                operation += 0
            else:
                operation += 1

        return operation

