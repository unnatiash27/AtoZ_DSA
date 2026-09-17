class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[c]=nums[i]
                c+=1
        return c