from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        
        max_freq = max(count.values())
        count_max = list(count.values()).count(max_freq)
        
        formula = (max_freq - 1) * (n + 1) + count_max
        
        return max(len(tasks), formula)