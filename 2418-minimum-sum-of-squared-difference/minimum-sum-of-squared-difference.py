class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff=[]
        k=k1+k2
        for i in range(len(nums1)):
            diff.append(abs(nums1[i]-nums2[i]))
        cnt=Counter(diff)
        maxi=max(cnt.keys())

        for i in range(maxi,0,-1):
            if k<=0:break
            sub=min(k,cnt[i])
            cnt[i]-=sub
            cnt[i-1]+=sub
            k-=sub
        res=0
        for d,v in cnt.items():
            res+=(d**2)*v
        return res