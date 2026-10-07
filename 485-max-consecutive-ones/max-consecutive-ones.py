class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans=0
        i=0
        j=0
        while j<len(nums):
            if nums[j]==0:
                i=j+1
                j+=1
            else:
                ans=max(ans,j-i+1)
                j+=1
        return ans