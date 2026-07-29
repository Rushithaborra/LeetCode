class Solution(object):
    def smallestPalindrome(self, s, k):
        from collections import Counter

        cnt = Counter(s)

        middle = ""
        freq = {}
        m = 0

        for ch in cnt:
            if cnt[ch] % 2:
                middle = ch

            freq[ch] = cnt[ch] // 2
            m += freq[ch]

        # Calculate nCr, but stop once it reaches k
        def comb(n, r):
            r = min(r, n - r)

            result = 1

            for i in range(1, r + 1):
                result = result * (n - r + i) // i

                if result >= k:
                    return k

            return result

        # Number of distinct permutations
        def count_permutations(remaining):
            result = 1
            used = 0

            for ch in freq:
                c = freq[ch]

                if c == 0:
                    continue

                ways = comb(used + c, c)
                result *= ways

                if result >= k:
                    return k

                used += c

            return result

        # Not enough palindromes
        if count_permutations(m) < k:
            return ""

        left = []

        # Build left half
        for pos in range(m):

            for ch in sorted(freq.keys()):

                if freq[ch] == 0:
                    continue

                # Try putting ch here
                freq[ch] -= 1

                ways = count_permutations(m - pos - 1)

                if k > ways:
                    # Skip all permutations starting with ch
                    k -= ways
                    freq[ch] += 1
                else:
                    # This character belongs here
                    left.append(ch)
                    break

        left = "".join(left)

        return left + middle + left[::-1]