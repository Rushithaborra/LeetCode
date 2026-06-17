class Solution(object):
    def processStr(self, s, k):
        n = len(s)

        # length after each operation
        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1
            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif ch == '#':
                lengths[i + 1] = cur * 2
            else:  # '%'
                lengths[i + 1] = cur

        final_len = lengths[n]

        if k < 0 or k >= final_len:
            return '.'

        # work backwards
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]
            cur = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == prev:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if k >= prev:
                    k -= prev

            else:  # '%'
                k = prev - 1 - k

        return '.'