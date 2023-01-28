class Solution:
    def fib(self, N: int) -> int:
        d={0:0,1:1}
        def fib(N):
            if N in d:
                return d[N]
            else:
                ans=fib(N-1) + fib(N-2)
                d[N]=ans
                return ans
        return (fib(N))
