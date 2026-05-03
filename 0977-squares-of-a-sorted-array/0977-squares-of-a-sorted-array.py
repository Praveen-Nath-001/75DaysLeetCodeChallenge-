class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [num**2 for num in nums]
        return sorted(output)

        