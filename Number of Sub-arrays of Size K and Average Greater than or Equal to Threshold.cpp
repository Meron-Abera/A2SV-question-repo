class Solution {
public:
  int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int ans = 0;
    int sum = 0;
    for (int i = 0; i < arr.size(); ++i) {
      sum += arr[i];
      if (i + 1 >= k) {
        if (threshold * k <= sum) ++ans;
        sum -= arr[i + 1 - k];
      } 
    }
    return ans;
  }
};
