class Solution:
    def corpFlightBookings(
        self,
        bookings: List[List[int]],
        n: int
    ) -> List[int]:
        acc = [0] * (n + 2)
        for b in bookings:
            acc[b[0]] += b[2]
            acc[b[1]+1] -= b[2]
        for i in range(1, n+1):
            acc[i] += acc[i-1]
        return acc[1:-1]
