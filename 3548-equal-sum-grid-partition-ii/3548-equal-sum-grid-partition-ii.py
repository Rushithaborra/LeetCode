from collections import Counter

class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        # -------- Horizontal cuts --------
        top_counter = Counter()
        bottom_counter = Counter()
        
        for row in grid:
            bottom_counter.update(row)
        
        top_sum = 0
        
        for i in range(m - 1):
            for val in grid[i]:
                top_counter[val] += 1
                bottom_counter[val] -= 1
                if bottom_counter[val] == 0:
                    del bottom_counter[val]
                top_sum += val
            
            bottom_sum = total - top_sum
            
            if top_sum == bottom_sum:
                return True
            
            diff = abs(top_sum - bottom_sum)
            
            if top_sum > bottom_sum:
                if self.check(top_counter, grid, 0, i, 0, n - 1, diff):
                    return True
            else:
                if self.check(bottom_counter, grid, i + 1, m - 1, 0, n - 1, diff):
                    return True
        
        # -------- Vertical cuts --------
        left_counter = Counter()
        right_counter = Counter()
        
        for j in range(n):
            for i in range(m):
                right_counter[grid[i][j]] += 1
        
        left_sum = 0
        
        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_counter[val] += 1
                right_counter[val] -= 1
                if right_counter[val] == 0:
                    del right_counter[val]
                left_sum += val
            
            right_sum = total - left_sum
            
            if left_sum == right_sum:
                return True
            
            diff = abs(left_sum - right_sum)
            
            if left_sum > right_sum:
                if self.check(left_counter, grid, 0, m - 1, 0, j, diff):
                    return True
            else:
                if self.check(right_counter, grid, 0, m - 1, j + 1, n - 1, diff):
                    return True
        
        return False
    
    def check(self, counter, grid, r1, r2, c1, c2, diff):
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        
        # Case 1: rectangle → just check existence
        if rows > 1 and cols > 1:
            return diff in counter
        
        # Case 2: single row
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff
        
        # Case 3: single column
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff
        
        return False