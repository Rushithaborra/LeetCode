class Solution(object):
    def minSetSize(self, arr):
        from collections import Counter
        freq = Counter(arr)              
        counts = sorted(freq.values(), reverse=True)  
        removed = 0
        half = len(arr) // 2
        result = 0
        for count in counts:             
            removed += count
            result += 1
            if removed >= half:
                return result