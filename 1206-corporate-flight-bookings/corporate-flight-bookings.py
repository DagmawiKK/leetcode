class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n
        
        for s, e, seats in bookings:
            result[s - 1] += seats  
            if e < n:
                result[e] -= seats  
        
        return accumulate(result)
