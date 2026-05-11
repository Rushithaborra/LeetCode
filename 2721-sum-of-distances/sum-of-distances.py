class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict        
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)   
        n = len(nums)
        ans = [0] * n
        for indices in pos.values():
            m = len(indices)
            prefix = [0]
            for x in indices:
                prefix.append(prefix[-1] + x)        
            for i in range(m):
                idx = indices[i]
                left = idx * i - prefix[i]
                right = (prefix[m] - prefix[i + 1]) - idx * (m - i - 1)
                ans[idx] = left + right
        
        return ans