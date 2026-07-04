# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:i for i, val in enumerate(inorder)}
        postorder_idx = len(postorder)-1

        def build(left, right):
            nonlocal postorder_idx
            # print(left,right)
            if left > right:        return None
            # print("postorder_idx",postorder_idx)
            root_val = postorder[postorder_idx]

            postorder_idx -=1

            # print("root_val",root_val)

            mid = inorder_map[root_val]
            # print("mid",mid)

            root = TreeNode(root_val)
            # print(f"build for left: {left,mid-1}")
            # print(f"build for right: {mid+1,right}")

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root

        return build(0,len(inorder)-1)
