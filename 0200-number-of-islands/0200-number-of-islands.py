class Solution:
    def checkIsland(self, grid, row, column):
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[row]) or grid[row][column] != '1':
            return
        
        grid[row][column] = '2'
        self.checkIsland(grid, row - 1, column)
        self.checkIsland(grid, row, column + 1)
        self.checkIsland(grid, row + 1, column)
        self.checkIsland(grid, row, column - 1)



    def numIslands(self, grid: List[List[str]]) -> int:
        totalIslands = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    self.checkIsland(grid, row, column)
                    totalIslands += 1
        
        return totalIslands