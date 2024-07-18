class Solution:
    def reverseVowels(self, s: str) -> str:
        strList = list(s)
        pt1 = 0
        pt2 = len(s) - 1 
        i = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while pt1 <= pt2 and i < len(strList):
            if strList[pt1] in vowels and strList[pt2] not in vowels:
                pt2 -=1
            elif strList[pt1] not in vowels and strList[pt2] in vowels:
                pt1 += 1

            elif strList[pt1] not in vowels and strList[pt2] not in vowels:
                pt2 -=1
                pt1 +=1
            elif strList[pt1] in vowels and strList[pt2] in vowels:
                strList[pt1], strList[pt2] = strList[pt2], strList[pt1]
                pt2 -=1
                pt1 +=1
            i += 1
        return ''.join(map(str, strList))
