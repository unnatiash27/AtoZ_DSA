class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mini=nums[0]
        # for i in nums:
        #     if (i < mini):
        #         mini=i
        # return mini


        # TLE
        # n=len(nums)
        # ans=0
        # i=0
        # j=nums[n-1]
        # while i<j:
        #     if nums[i]>nums[j]:
        #         i+=1
        #     else:
        #         ans=nums[i]
        # return ans

        n=len(nums)
        l=0
        h=n-1
        mini=nums[0]

        while(l<=h):
            mid=(l+h)//2
            if nums[l]<=nums[mid]:
                mini=min(mini,nums[l])
                l=mid+1
            else:
                mini=min(mini,nums[mid])
                h=mid-1
        return mini