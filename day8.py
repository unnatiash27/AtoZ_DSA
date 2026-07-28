class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        n=len(nums)
        i=0
        ans=[]
        # while i<n:
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             ans.append(i+1)
        #             ans.append(j+1)
        #     i+=1
        j=n-1
        while i<j:
            if nums[i]+nums[j] > t:
                j-=1
            elif nums[i]+nums[j] < t:
                i+=1
            else:
                ans.append(i+1)
                ans.append(j+1)
                break
        return ans
      
