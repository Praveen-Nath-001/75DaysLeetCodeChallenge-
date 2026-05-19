# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # I see one of the targets! I will inform my caller!
        if root == q or root == p: return root
        
        # Look in the left, if you find p or q , return yourself
        foundInLeft = self.lowestCommonAncestor(root.left, p, q)
        
        # Look in the right, if you find p or q , return yourself
        foundInRight = self.lowestCommonAncestor(root.right, p, q)
        
        # Didnt find anything in the left, must be in right
        if not foundInLeft: return foundInRight
        
        # Didnt find anything in the right, must be in the left
        if not foundInRight: return foundInLeft
        
        # Found something in both! Hence this is the one!
        return root