class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        min_ele = float('inf')
        for i in range(n):
            min_ele = min(nums[i], min_ele)
        return min_ele