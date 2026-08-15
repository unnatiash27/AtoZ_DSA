class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        #             break
        # return False

        # mp={}
        # for i in nums:
        #     if i in mp and mp[i]>=1:
        #         return True
        #     mp[i]=mp.get(i,0)+1
        # return False

        hset=set()
        for i in nums:
            if i in hset:
                return True
            hset.add(i)
        return False
