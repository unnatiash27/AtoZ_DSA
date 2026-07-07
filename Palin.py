class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        nd=0
        num=x
        while(x!=0):
            d=x%10
            nd=nd*10+d
            x=x//10
        if nd==num:
            return True
        else:
            return False
