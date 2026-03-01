class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr =[(num,i) for i,num in enumerate(nums)]
        arr.sort()
        left,right=0,len(nums)-1
        while left<right:
            sum = arr[left][0] + arr[right][0]
            if(sum==target):
                return(arr[left][1] , arr[right][1])
            elif(sum<target):
                left+=1
            else: 
                right-=1

        return[left,right]
        