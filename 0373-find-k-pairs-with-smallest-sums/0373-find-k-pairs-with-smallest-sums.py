import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        result = []
        
        # Push first element from nums2 for each element in nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract k smallest pairs
        while k > 0 and min_heap:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # Move to next element in nums2
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
            
            k -= 1
        
        return result