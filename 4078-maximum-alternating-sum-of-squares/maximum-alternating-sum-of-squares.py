class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr=[]
        ans=0
        for i in range(len(nums)):
            arr.append(nums[i]*nums[i])
        
        arr.sort()

        i=0
        j=len(nums)-1
        while(i<j):
            ans+=arr[j]-arr[i]
            i+=1
            j-=1
        if i==j:
            ans+=arr[i]
        
        return ans