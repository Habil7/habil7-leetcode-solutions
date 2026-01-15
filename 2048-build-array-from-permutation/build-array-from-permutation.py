class Solution:
    def buildArray(self, lst: List[int]) -> List[int]:
        last_version = []

        for i in range(len(lst)):
            last_version += [lst[lst[i]]]

        return last_version
    
