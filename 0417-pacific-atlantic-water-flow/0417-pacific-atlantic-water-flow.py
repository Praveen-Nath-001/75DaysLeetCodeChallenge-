class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights:
            return []
        
        m = len(heights)
        n = len(heights[0])
        
        pac = [[False]*n for _ in range(m)]
        atl = [[False]*n for _ in range(m)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited):
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                
                if visited[nr][nc]:
                    continue
                
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr, nc, visited)
        
        
        # Pacific: top row + left col
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)
        
        # Atlantic: bottom row + right col
        for c in range(n):
            dfs(m-1, c, atl)
        for r in range(m):
            dfs(r, n-1, atl)
        
        
        result = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])
        
        return result