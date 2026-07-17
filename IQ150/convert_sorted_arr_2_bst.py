# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        total_nodes = len(nums)
        if not nums:
            return None
        
        mid = total_nodes//2

        bst = TreeNode(nums[mid], left = self.sortedArrayToBST(nums[:mid]),
                                  right = self.sortedArrayToBST(nums[mid + 1:]))
        return bst
