class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        count = 0
        left = 0
        while tickets[k] > 0:
            if left == len(tickets):
                left = 0

            tickets[left] -= 1
            
            if tickets[left] < 0:
                left += 1
                continue
            left += 1
            count += 1
        return count

