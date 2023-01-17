class Solution {
   public int[] productExceptSelf(int[] nums) {
    int[] res = new int[nums.length];
    res[0] = 1;
    res[nums.length-1] = 1;
    int n = 1;
    int k = nums.length-2;
    int fromLeft = 1;
    int fromRight = 1;
    while(n < nums.length) {
        fromLeft  = nums[n-1] * fromLeft;
        fromRight = nums[k+1] * fromRight;
        if (n < k) {
            res[n] = fromLeft;
            res[k] = fromRight;
        } else {
            if (n == k) {
                res[n] = fromLeft * fromRight;
            } else {
                res[n] = fromLeft  * res[n];
                res[k] = fromRight * res[k];
            }
        }
        n++;
        k--;
    }
    return res;
}
}
