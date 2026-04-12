# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        res = []
        while curr :
            res.append(curr.val)
            curr = curr.next
        ans = ListNode()
        ans.next = head
        left = 0
        right = len(res)-1
        while left<=right and head.next:
            head.val = res[left]
            head.next.val = res[right]
            head = head.next.next
            left+=1
            right-=1
            if left == right:
                head.val = res[left]
                break
        
        return ans.next