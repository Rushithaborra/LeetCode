import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        min_heap = []
        for j in range(1, n):
            heapq.heappush(min_heap, (arr[0]/float(arr[j]), 0, j))
        for _ in range(k - 1):
            value, i, j = heapq.heappop(min_heap)
            
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i+1]/float(arr[j]), i+1, j))
        
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]