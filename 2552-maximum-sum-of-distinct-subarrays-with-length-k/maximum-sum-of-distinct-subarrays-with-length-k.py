class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        i=0
        j=0
        sumi=0
        res=0
        visi=set()
        while j<len(nums):
            while nums[j] in visi:
                sumi-=nums[i]
                visi.remove(nums[i])
                i+=1
            sumi+=nums[j]
            visi.add(nums[j])
            if (j-i+1)==k:
                res=max(res,sumi)
                sumi-=nums[i]
                visi.remove(nums[i])
                i+=1
            j+=1
        return res
