class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # base cases 
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def dp(array):
            n = len(array)
            
            memo = [0] * n
            memo[0] = array[0] 
            memo[1] = max(array[:2])

            for i in range(2, n):
                memo[i] = max(memo[i-1], memo[i-2] + array[i])
            
            return memo[-1]

        return max(dp(nums[:len(nums)-1]), dp(nums[1:len(nums)]))