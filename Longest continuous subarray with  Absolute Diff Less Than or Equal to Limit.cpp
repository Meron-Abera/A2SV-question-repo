class Solution {
public:
   int longestSubarray(vector<int>& nums, int k) {
      int ret = 0;
      int i = 0;
      int j = 0;
      deque<int> maxD;
      deque<int> minD;
      int n = nums.size();
      for (int i = 0; i < n; i++) {
         while (!maxD.empty() && maxD.back() < nums[i])
            maxD.pop_back();
         while (!minD.empty() && minD.back() > nums[i])
            minD.pop_back();
         maxD.push_back(nums[i]);
         minD.push_back(nums[i]);
         while (maxD.front() - minD.front() > k) {
            if (nums[j] == maxD.front())
               maxD.pop_front();
            if (nums[j] == minD.front())
               minD.pop_front();
            j++;
         }
         ret = max(ret, i - j + 1);
      }
      return ret;
   }
};
