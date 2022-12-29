class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        s=[]
        for i in nums:
            c=0
            for j in n:
                if j<i:
                    c+=1
                else:
                    break
            s.append(c)
        return (s)
