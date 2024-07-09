class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = []
        current_time = 0
        for i in customers:
            arrival, time_to_prepare = i
            current_time = max(current_time, arrival) + time_to_prepare
            wait_time.append(current_time - arrival)
        return (sum(wait_time) / len(wait_time))