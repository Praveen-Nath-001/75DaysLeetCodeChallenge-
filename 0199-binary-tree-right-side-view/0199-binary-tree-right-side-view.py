# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        out = []
        q = deque([root])

        while q:
            next_q = deque()
            while q:        # iterate over all eles in current level. build next level (next_q)
                e = q.popleft()
                rightmost = e.val      # overwrite prev rightmost val since this is more right

                if e.left:      # add children if any
                    next_q.append(e.left)
                if e.right:
                    next_q.append(e.right)

            out.append(rightmost) # add rightmost val of the level
            q = next_q      # set q for the next level

        return out