class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxp=minp=ans=nums[0]
        for x in nums[1:]:
            if x<0:
                maxp,minp=minp,maxp
            maxp=max(x,maxp*x)
            minp=min(x,minp*x)
            ans=max(ans,maxp)
        return ans