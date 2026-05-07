class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        maximum = 0
        hashmap= defaultdict(int)
        for r in range(len(fruits)):
            hashmap[fruits[r]]+=1
            if len(hashmap)>2:
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]] ==0:
                    del hashmap[fruits[l]]
                l+=1
            maximum = max(maximum, r - l + 1)
        return maximum

        