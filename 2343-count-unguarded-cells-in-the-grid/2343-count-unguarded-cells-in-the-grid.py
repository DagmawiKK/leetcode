class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        array = [[0 for x in range(n)]for x in range(m)]

        for row, col in guards:
            array[row][col] = "G"

        for row, col in walls:
            array[row][col] = "W"
        
        def marker(row, col, directionX, directionY):
            while 0 <= row < m and 0 <= col < n:
                if array[row][col] == "W" or array[row][col] == "G":
                    break
                if array[row][col] == 0:
                    array[row][col] = 1
                row += directionX
                col += directionY

        for row, col in guards:
            marker(row, col-1, 0, -1)
            marker(row, col +1 , 0, +1)
            marker(row+1, col, +1, 0)
            marker(row-1, col, -1, 0)
        count = 0
        for i in range(m):
            for j in range(n):
                if array[i][j] == 0:
                    count += 1
        return count 