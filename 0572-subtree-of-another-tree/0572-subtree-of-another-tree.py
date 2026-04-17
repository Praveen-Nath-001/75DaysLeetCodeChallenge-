# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def solve(root, subRoot, contig):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            if contig:
                if root.val != subRoot.val:
                    return False
                return solve(root.left, subRoot.left, True) and solve(root.right, subRoot.right, True)
                
            return (
                solve(root.left, subRoot, False) or
                solve(root.right, subRoot, False) or
                solve(root, subRoot, True)
            )
            
        return solve(root, subRoot, False)