class Solution(object):
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2 + 3
        for row in matrix:
            row.sort(reverse=True)  # rearranging columns
            
            for i in range(n):
                area = row[i] * (i + 1)
                max_area = max(max_area, area)
        
        return max_area