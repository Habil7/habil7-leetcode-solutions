# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left_index, right_index):
            if left_index > right_index:
                return None

            middle_index = (left_index + right_index) // 2

            root = TreeNode(nums[middle_index])

            root.left = build_bst(left_index, middle_index - 1)
            root.right = build_bst(middle_index + 1, right_index)

            return root

        return build_bst(0, len(nums) - 1)