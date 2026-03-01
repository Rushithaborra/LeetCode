import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        for _ in range(k-1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
        return heapq.heappop(min_heap)[0]