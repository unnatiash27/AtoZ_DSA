class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        self.help("",0,0,ans,n)
        return ans

    def help(self,st:str,open:int,close:int,ans:list,n:int):
        # base condin
        if len(st) == n*2:
            ans.append(st)
            return
        if open<n:
            self.help(st+"(",open+1,close,ans,n)
        if close < open:
            self.help(st+")",open,close+1,ans,n)