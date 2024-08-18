class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)

        for first, last, seats in bookings:
            answer[first] += seats
            if last + 1 < n+1:
                answer[last+1] -= seats
        
        answer = list(accumulate(answer))
        
        return answer[1:]
