class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = []
        count_map = Counter(tasks)
        max_heap = [-freq for freq in count_map.values()]
        heapq.heapify(max_heap)
        
        while max_heap or queue:
            time+=1
            if max_heap:
               task_freq = 1+heapq.heappop(max_heap)
               if task_freq:
                  queue.append([task_freq,time+n])
            if queue and queue[0][1]==time:
               heapq.heappush(max_heap,queue.pop(0)[0])
        return time