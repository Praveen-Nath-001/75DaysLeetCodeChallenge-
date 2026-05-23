class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        while len(stones) > 1:
            first, second, stones = stones[0], stones[1], stones[2:]
            if first != second:
                stones.append(abs(first - second))
                stones.sort(reverse=True)
        return stones[0] if stones else 0 