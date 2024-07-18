class Solution:
    def reverseVowels(self, s: str) -> str:
        strList = list(s)
        pt1 = 0
        pt2 = len(s) - 1 
        i = 0
        vowles = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        while pt1 <= pt2 and i < len(strList):
            if strList[pt1] in vowles and strList[pt2] not in vowles:
                pt2 -=1
            elif strList[pt1] not in vowles and strList[pt2] in vowles:
                pt1 += 1

            elif strList[pt1] not in vowles and strList[pt2] not in vowles:
                pt2 -=1
                pt1 +=1
            elif strList[pt1] in vowles and strList[pt2] in vowles:
                strList[pt1], strList[pt2] = strList[pt2], strList[pt1]
                pt2 -=1
                pt1 +=1
            i += 1
        return ''.join(map(str, strList))
