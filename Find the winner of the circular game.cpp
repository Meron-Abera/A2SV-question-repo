class Solution {
public:
    int findTheWinner(int n, int k) {
        queue<int> players;
        int xorr=0;
        for(int i=1;i<=n;i++){
            players.push(i);
            xorr^=i;
        }
        
        int kt=0;
        while(players.size()!=1){
            kt++;
            int val=players.front();
            if(kt==k){
                kt=0;
                players.pop();
                xorr^=val;
                continue;
            }
            players.push(val);
            players.pop();
        }
        return xorr;
    }
};
