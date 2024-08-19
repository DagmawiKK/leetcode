class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i, tickets[i]) for i in range(len(tickets)))
        time = 0
        while queue:
            index, value = queue.popleft()
            value -= 1

            if index == k and value == 0:
                time += 1
                return time
            
            if value > 0:
                queue.append((index, value))

            time += 1

        return time
