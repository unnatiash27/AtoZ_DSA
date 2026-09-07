class Solution {
public:
    int maxProfit(vector<int>& p) {
        int mini=p[0],pr=0,c;
        for(int i=0;i<p.size();i++)
        {
            c=p[i]-mini;
            pr=max(pr,c);
            mini=min(mini,p[i]);
        }
        return pr;
    }
};