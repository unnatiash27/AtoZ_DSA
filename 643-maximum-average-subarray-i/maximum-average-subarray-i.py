class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i=0
        j=k
        sumi=0
        for i in range(0,k):
            sumi+=nums[i]
        temp=sumi
        i=0
        while i<len(nums) and j<len(nums):
            sumi+=nums[j]-nums[i]
            i+=1
            j+=1
            temp=max(temp,sumi)

        return temp/k