class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            j = len(row) - 1

            while i <= j:
                if row[i] == row[j]:
                    row[i] = row[j] = 1 - row[i]
                i += 1
                j -= 1

        return image

