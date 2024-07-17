class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in image:
            a, b = 0, len(i) - 1

            while a <= b:
                if i[a] == i [b]:
                    i[a], i[b] = 1 - i[a], 1 - i[b]
                a += 1
                b -= 1
        return image