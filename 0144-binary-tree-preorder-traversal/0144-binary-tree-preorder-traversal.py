# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def preorder_helper(self, root):
        if root is None:
            return 
        self.ans.append(root.val)
        self.preorder_helper(root.left)
        self.preorder_helper(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # self.ans =[]
        self.preorder_helper(root)
        return self.ans