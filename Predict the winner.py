from functools import lru_cache
from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:
            return None
        
        @lru_cache(maxsize=None)
        def bestScoreAdvantage(lo, hi):
            if lo > hi:
                return 0
            return max(
                nums[lo] - bestScoreAdvantage(lo+1, hi),
                nums[hi] - bestScoreAdvantage(lo, hi-1)
            )
            
        return bestScoreAdvantage(0, len(nums)-1) >= 0
