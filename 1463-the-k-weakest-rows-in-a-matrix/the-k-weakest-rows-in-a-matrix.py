class Solution(object):
    def kWeakestRows(self, mat, k):
        
        def count_soldiers(row):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        arr = []
        
        for i, row in enumerate(mat):
            arr.append((count_soldiers(row), i))
        
        arr.sort()
        
        return [index for _, index in arr[:k]]