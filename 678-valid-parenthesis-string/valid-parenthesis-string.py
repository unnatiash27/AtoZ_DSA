class Solution:
    def checkValidString(self, s: str) -> bool:
        st=[]
        star=[]

        for i in range (0,len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if st:
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while  st and  star:
            if st[-1]<star[-1]:
                st.pop()
                star.pop()
            else:
                star.pop()
        if not st:
            return True
        else:
            return False