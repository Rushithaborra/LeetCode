class Solution(object):
    def longestWord(self, words):
        words.sort()
        s = set()
        ans = ""

        for word in words:
            if len(word) == 1 or word[:-1] in s:
                s.add(word)

                if len(word) > len(ans):
                    ans = word

        return ans