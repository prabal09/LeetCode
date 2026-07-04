# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left_node,right_node):
            if not left_node and not right_node:      return True
            if (left_node and not right_node) or (right_node and not left_node) :      return False
            if left_node.val != right_node.val:       return False

            return symmetric(left_node.left,right_node.right) and symmetric(left_node.right, right_node.left)
        return symmetric(root,root)
