class Solution:
    def maxSumOfSquares(self, num: int, sumi: int) -> str:
        ans=""
        if num*9 <sumi:
            return ans
            # break
        
        
        while num!=0:
            dig=min(9,sumi)
            # nex=sumi-dig
            ans+=str(dig)
            sumi-=dig
            # dig=nex
            num-=1
        return ans