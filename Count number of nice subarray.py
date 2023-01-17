class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # mod number to 2, change the question to subarray sum to k
        cur_sum = res = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            cur_sum += nums[i] % 2
            if cur_sum - k in dic:
                res += dic[cur_sum-k]
            dic[cur_sum] += 1
        return res
