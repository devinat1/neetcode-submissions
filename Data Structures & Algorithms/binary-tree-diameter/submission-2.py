# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global_max = 0
        def r(node):
            nonlocal global_max
            if not node:
                return 0
            left_height = r(node.left)
            right_height = r(node.right)
            global_max = max(global_max, left_height + right_height)
            return 1 + max(left_height, right_height)

        r(root)
        return global_max