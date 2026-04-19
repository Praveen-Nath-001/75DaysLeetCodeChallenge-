# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = 0
        def get_height(node):
            nonlocal largest_diameter  

            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            current_diameter = left_height + right_height
            largest_diameter = max(largest_diameter, current_diameter)
            return max(left_height, right_height) + 1

        get_height(root)
        return largest_diameter