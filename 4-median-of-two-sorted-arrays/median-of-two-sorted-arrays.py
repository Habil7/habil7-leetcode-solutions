class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        lenA, lenB = len(A), len(B)
        left, right = 0, lenA

        while left <= right:
            cutA = (left + right) // 2
            cutB = (lenA + lenB + 1) // 2 - cutA

            leftA  = A[cutA - 1] if cutA > 0 else float("-inf")
            rightA = A[cutA] if cutA < lenA else float("inf")

            leftB  = B[cutB - 1] if cutB > 0 else float("-inf")
            rightB = B[cutB] if cutB < lenB else float("inf")

            # correct split found
            if leftA <= rightB and leftB <= rightA:
                if (lenA + lenB) % 2 == 1:
                    return float(max(leftA, leftB))
                return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                right = cutA - 1
            else:
                left = cutA + 1