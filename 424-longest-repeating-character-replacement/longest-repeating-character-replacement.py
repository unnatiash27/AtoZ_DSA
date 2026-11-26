class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=0
        mf=0
        cnt=[0]*26
        for r in range(len(s)):
            cnt[ord(s[r])-ord('A')]+=1
            mf=max(mf, cnt[ord(s[r])-ord('A')])
            while ((r-l+1) -mf > k) :
                cnt[ord(s[l])-ord('A')]-=1
                l+=1
            ans=max(ans, r-l+1)
        return ans