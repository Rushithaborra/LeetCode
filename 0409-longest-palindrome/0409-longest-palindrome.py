class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        length = 0
        odd_found = False
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        if odd_found:
            length += 1

        return length