class TimeMap:

    def __init__(self):
        self.dic={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key]=[]
        self.dic[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        val=self.dic.get(key,[])
        l,r=0 ,len(val)-1
        while l<=r:
            mid=(l+r)>>1
            if val[mid][1]<=timestamp:
                l=mid+1
                res=val[mid][0]
            else:
                r=mid-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)