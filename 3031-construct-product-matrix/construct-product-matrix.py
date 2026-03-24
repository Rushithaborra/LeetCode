class Solution(object):
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = n * m
    
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        res = [0] * size
        for i in range(size):
            res[i] = (prefix[i] * suffix[i]) % MOD
        
        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(res[idx])
                idx += 1
            ans.append(row)
        
        return ans