class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        longest = 1
        unique_val = set()
        for i in range(n):
            unique_val.add(nums[i])

        for ele in unique_val:
            if ele - 1 not in unique_val:
                cnt = 1
                x = ele
                while x + 1 in unique_val:
                    x += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest

            