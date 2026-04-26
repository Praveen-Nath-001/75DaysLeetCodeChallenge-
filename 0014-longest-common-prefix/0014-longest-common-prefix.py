class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_1 = min(strs)
        str_2 = max(strs)
        idx = 0
        while idx< len(str_1):
            if str_1[idx] != str_2[idx]:
                str_1 = str_1[:idx]
            idx += 1
        return str_1        