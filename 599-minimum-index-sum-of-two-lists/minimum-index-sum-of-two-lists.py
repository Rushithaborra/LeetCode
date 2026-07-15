class Solution(object):
    def findRestaurant(self, list1, list2):
        if len(list1) > len(list2):
            list1, list2 = list2, list1

        mp = {v: i for i, v in enumerate(list1)}
        ans = []
        best = float('inf')

        for j, s in enumerate(list2):
            if s in mp:
                t = mp[s] + j
                if t < best:
                    best = t
                    ans = [s]
                elif t == best:
                    ans.append(s)

        return ans