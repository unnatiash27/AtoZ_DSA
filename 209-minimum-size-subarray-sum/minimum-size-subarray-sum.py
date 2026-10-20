class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans=len(nums)+1
        i=0
        j=0
        sumi=0

        for j in range(len(nums)):
            sumi+=nums[j]
            while sumi>=target:
                ans=min(ans,j-i+1)
                sumi-=nums[i]
                i+=1
        
        return ans if ans!=len(nums)+1 else 0