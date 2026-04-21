# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = []
        result = []

        queue.append(root)

        while queue:
            current_level = []
            current_length = len(queue)
            
            for _ in range(current_length):
                current_node = queue.pop(0)
                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
                
            result.append(current_level)
        
        return result
        