class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            j = len(row) - 1

            while i <= j:
                if row[i] == row[j]:
                    if row[i] == 0:
                        row[j] = row[i] = 1
                    else:
                        row[j] = row[i] = 0
                i += 1
                j -= 1

        return image

