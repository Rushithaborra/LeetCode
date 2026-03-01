1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        arr =[(num,i) for i,num in enumerate(nums)]
9        arr.sort()
10        left,right=0,len(nums)-1
11        while left<right:
12            sum = arr[left][0] + arr[right][0]
13            if(sum==target):
14                return(arr[left][1] , arr[right][1])
15            elif(sum<target):
16                left+=1
17            else: 
18                right-=1
19
20        return[left,right]
21        