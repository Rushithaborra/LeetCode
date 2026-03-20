class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                arr = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        arr.append(grid[x][y])

                arr.sort()

                min_diff = float('inf')
                for t in range(len(arr) - 1):
                    if arr[t] != arr[t + 1]:  
                        min_diff = min(min_diff, arr[t + 1] - arr[t])

                if min_diff == float('inf'):
                    min_diff = 0

                row.append(min_diff)

            result.append(row)

        return result