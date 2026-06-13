class Solution(object):
    def mapWordWeights(self, words, weights):
        result = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            result.append(chr(ord('z') - (total % 26)))

        return ''.join(result)