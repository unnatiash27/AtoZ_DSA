class Solution:
    def minInsertions(self, s: str) -> int:
        ans=0
        st=[]
        i=0
        while i<len(s):
            if s[i]=="(":
                st.append('(')
                i+=1
            else:
                if i+1 <len(s) and s[i+1]==")":
                    i=i+2
                else:
                    i+=1
                    ans+=1
                if st:
                    st.pop()
                else:
                    ans+=1
        ans+= 2*len(st)
        return ans