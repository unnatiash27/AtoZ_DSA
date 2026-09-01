class Solution:
    def search(self, nums: List[int], t: int) -> int:
        # if ans==target:
        #     return i
        # else:
        #     return -1
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=i + (j-i) // 2
            if t == nums[mid]:
                return mid
            elif t<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        return -1
