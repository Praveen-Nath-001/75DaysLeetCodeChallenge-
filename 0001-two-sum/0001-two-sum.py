class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, num in enumerate(nums):
            diff  = target - num
            if diff in output:
                return  [output[diff], i]
            output[num] = i   
        