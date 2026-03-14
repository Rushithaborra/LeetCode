class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            
            for ch in ['a', 'b', 'c']:
                if not s or s[-1] != ch:
                    backtrack(s + ch)

        backtrack("")

        if k > len(res):
            return ""
        return res[k-1]