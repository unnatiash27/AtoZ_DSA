class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h :
            mid =(l+h)//2

            if nums[mid]==t:
                return mid
                break
            
            if nums[l]<=nums[mid]:
                if nums[l]<=t and nums[mid]>t:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<t and nums[h]>=t:
                    l=mid+1
                else:
                    h=mid-1

        return -1   