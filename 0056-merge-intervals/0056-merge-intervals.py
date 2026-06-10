class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals) 
        intervals.sort()
        output = []

        for i in range(n):
            if not output or intervals[i][0] > output[-1][1]:
                output.append(intervals[i])
          
            else:
                output[-1][1] = max(output[-1][1], intervals[i][1])
        return output

            