
class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        size = 4 * n
        total = [0] * size
        squares = [0] * size
        lazy = [0] * size

        def apply(node, l, r, val):
            length = r - l + 1
            squares[node] += 2 * val * total[node] + val * val * length
            total[node] += val * length
            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            apply(node * 2, l, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, r, lazy[node])
            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            total[node] = total[node * 2] + total[node * 2 + 1]
            squares[node] = squares[node * 2] + squares[node * 2 + 1]

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            ans += squares[1]
            last[x] = i

        return ans% (10**9 + 7)
