# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(node, side = 'left'):
            h = 0
            while node:
                h+=1
                if side == 'left':
                    node = node.left
                else:
                    node = node.right
            return h

        if not root:
            return 0

        l_ht = height(root)
        r_ht = height(root,'right')
        if l_ht == r_ht:
            return (1<<l_ht) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
