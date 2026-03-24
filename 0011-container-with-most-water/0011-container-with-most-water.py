class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_area = 0
        while low < high:
            area = min(height[low], height[high]) * (high - low)
            max_area = max(area, max_area)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area
