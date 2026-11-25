class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lf=0
        lent=0
        mp={}
        for ri in range(len(s)):
            if s[ri] not in mp or mp[s[ri]]<lf:
                mp[s[ri]]=ri
                lent=max(lent,ri-lf+1)
            else:
                lf=mp[s[ri]]+1
                mp[s[ri]]=ri
        return lent