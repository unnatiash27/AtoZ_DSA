class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        dictt={}
        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            
            if not st:
                dictt[nums2[i]]=-1
            else:
                dictt[nums2[i]]=st[-1]
            
            st.append(nums2[i])
        
        final=[]
        for i in nums1:
            final.append(dictt[i])

        return final
