# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count Total Nodeds 
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        #Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        #Move to node before target
        prev = dummy
        for _ in range(count - n):
            prev = prev.next
        
        #Delete node
        prev.next = prev.next.next
        
        return dummy.next
        