class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        chars = set(word)
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in chars and ch.upper() in chars:
                count += 1

        return count