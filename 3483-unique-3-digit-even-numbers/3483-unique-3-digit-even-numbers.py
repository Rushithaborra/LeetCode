class Solution:
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            if [a, b, c].count(a) <= digits.count(a) and \
               [a, b, c].count(b) <= digits.count(b) and \
               [a, b, c].count(c) <= digits.count(c):
                count += 1

        return count