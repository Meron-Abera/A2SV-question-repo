class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        vector<int>emp;
        if(changed.size()%2!=0) return emp;
        sort(changed.begin(),changed.end());
        unordered_map<int,int>mp;
        for(auto a:changed)
            mp[a]++;
        vector<int>ans;
       for(auto i:changed){
            if(mp[i]==0) continue;
             if(mp[i*2]==0) return emp;
                  ans.push_back(i);
                 mp[i]--;
                  mp[i*2]--;
       }
        return ans;
    }
};
