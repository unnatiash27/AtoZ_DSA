class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            hrs=0
            for x in piles:
                hrs+=x//mid
                if x%mid!=0:
                    hrs+=1
            if hrs<=h:
                high=mid
            else:
                low=mid+1
        return low