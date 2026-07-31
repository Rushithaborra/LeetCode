class Solution(object):
    def minimumPushes(self, word):
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        ans = 0

        for i in range(26):
            ans += freq[i] * (i // 8 + 1)

        return ans