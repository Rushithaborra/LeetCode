class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k
        nxt = primes[:]

        for i in range(1, n):
            mn = min(nxt)
            ugly[i] = mn

            for j in range(k):
                if nxt[j] == mn:
                    idx[j] += 1
                    nxt[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]