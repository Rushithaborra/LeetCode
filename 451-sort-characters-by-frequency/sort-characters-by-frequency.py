class Solution(object):
    def frequencySort(self, s):
        from collections import Counter      
        count = Counter(s)  
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for char, freq in sorted_chars:
            result += char * freq
        return result