class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1 # Left pointer
            k = n - 1 # Right pointer
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > 0:
                    # Sum is too large
                    k -= 1
                elif total < 0:
                    # Sum is too small
                    j += 1
                else:
                    # Found a triplet
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    # Skip duplicate values for the second element
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        
        return res
        