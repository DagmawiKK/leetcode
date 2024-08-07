class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n
        
        for s, e, seats in bookings:
            result[s - 1] += seats  
            if e < n:
                result[e] -= seats  

        for i in range(1, n):
            result[i] += result[i - 1]
        
        return result
