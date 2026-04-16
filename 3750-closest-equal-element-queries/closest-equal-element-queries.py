from collections import defaultdict
import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = []
        
        for q in queries:
            indices = pos[nums[q]]
            
            if len(indices) == 1:
                res.append(-1)
                continue
            
            i = bisect.bisect_left(indices, q)
            
            prev_idx = indices[i-1] if i > 0 else indices[-1]
            next_idx = indices[i+1] if i < len(indices)-1 else indices[0]
            
            d1 = abs(q - prev_idx)
            d2 = abs(q - next_idx)
            
            dist1 = min(d1, n - d1)
            dist2 = min(d2, n - d2)
            
            res.append(min(dist1, dist2))
        
        return res