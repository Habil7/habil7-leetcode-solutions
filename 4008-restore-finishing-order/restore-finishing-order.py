class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        answer = []

        for i in order:
            if i in friends:
                answer += [i]

        return answer

