class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n =len(matrix)

        martix2 = [[0 for i in range(n)] for j in range(n)]

        for r in range(n):
            for c in range(n):
                martix2[c][n - 1 - r] = matrix[r][c]
        for r in range(n):
            for c in range(n):
                matrix[r][c] = martix2[r][c]

                