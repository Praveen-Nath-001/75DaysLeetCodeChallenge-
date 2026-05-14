class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eating_rate = 1
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            total_hour = 0

            for bananas in piles:
                if bananas % mid == 0:
                    total_hour += bananas // mid
                else:
                    total_hour += bananas // mid + 1

            if total_hour <= h:
                min_eating_rate = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_eating_rate
        