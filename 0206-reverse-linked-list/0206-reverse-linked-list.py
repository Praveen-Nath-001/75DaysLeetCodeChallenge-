# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        nxt_node = None
        prev_node = None
        while curr_node != None:
            nxt_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = nxt_node

        return prev_node    
            
         

        