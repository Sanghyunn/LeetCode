class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0
        
        for column in range(0, len(grid)):
            for row in range(0, len(grid[0])):
                if grid[column][row] == 1:
                    area = self.search(grid, row, column)
                    max_area = max(max_area, area)
        
        return max_area
                    
        
    def search(self, grid, row, column):
        max_row = len(grid[0]) - 1
        max_column = len(grid) - 1
        
        grid[column][row] = 0
        area = 1
        
        if row != 0 and grid[column][row - 1] == 1 :
            area += self.search(grid, row - 1, column)
        if row != max_row and grid[column][row + 1] == 1:
            area += self.search(grid, row + 1, column)
        if column != 0 and grid[column - 1][row] == 1 :
            area += self.search(grid, row, column - 1)
        if column != max_column and grid[column + 1][row]:
            area += self.search(grid, row, column + 1)
        
        return area
            
        
        
        
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        