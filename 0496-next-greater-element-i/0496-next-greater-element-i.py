class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []                
        nxt_greater = {}         
        
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()            
                nxt_greater[smaller] = num     
            stack.append(num)                    

        for num in stack:
            nxt_greater[num] = -1              
        return [nxt_greater[num] for num in nums1]            