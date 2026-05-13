class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) 
        for num in range(n):
            if (num == 0 or nums[num - 1] < nums[num]) and (num == n - 1 or nums[num] > nums[num + 1]):
                return num

        return -1
            