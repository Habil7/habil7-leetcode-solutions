class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for idx, num in enumerate(nums):
            inverse = target - num
            if inverse in num_indices:
                return [num_indices[inverse], idx]
            num_indices[num] = idx
            