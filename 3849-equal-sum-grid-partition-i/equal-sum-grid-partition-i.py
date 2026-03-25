class Solution(object):
    def canPartitionGrid(self, grid):
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        curr = 0
        for i in range(len(grid) - 1):
            curr += sum(grid[i])
            if curr == target:
                return True
        
        cols = len(grid[0])
        col_sum = [0] * cols
        
        for row in grid:
            for j in range(cols):
                col_sum[j] += row[j]
        
        curr = 0
        for j in range(cols - 1):
            curr += col_sum[j]
            if curr == target:
                return True
        
        return False