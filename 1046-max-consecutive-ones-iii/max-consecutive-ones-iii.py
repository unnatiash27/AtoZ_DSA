class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zer=0
        i=0
        ans=0
        for j in range(0,len(nums)):
            if nums[j]==0:
                zer+=1
            while zer>k:
                if nums[i]==0:
                    zer-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans