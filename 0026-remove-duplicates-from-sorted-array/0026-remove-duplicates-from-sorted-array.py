class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = 0
        for b in range(1,len(nums)):
            if nums[a] != nums[b]:
                a += 1
                nums[a] = nums[b]
                
        return a+1 
        

        