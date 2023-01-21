class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(A)-1
        scan = 0
        
        while scan<=r:
            if A[scan]==0:
                A[scan],A[l] = A[l],A[scan]
                l+=1
                scan+=1
            elif A[scan]==2:
                A[scan],A[r] = A[r],A[scan]
                r-=1
            else:
                scan+=1
        return(A)
