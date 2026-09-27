class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        # freq=counter(nums)
        hashm={}
        cnt=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                cnt+=1
            else:
                if (nums[i],nums[i+1]) in hashm:
                    hashm[(nums[i],nums[i+1])]+=1
                elif (nums[i+1],nums[i]) in hashm:
                    hashm[(nums[i+1],nums[i])]+=1
                else:
                    hashm[(nums[i],nums[i+1])]=1
        maxi=float('-inf')
        for i in hashm:
            if hashm[i]>maxi:
                maxi=hashm[i]

        if maxi!=float('-inf'):
            cnt+=maxi
        return cnt
        