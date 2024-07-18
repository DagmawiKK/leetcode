class Solution:
    def reverseVowels(self, s: str) -> str:
        strList = list(s)
        pt1 = 0
        pt2 = len(s) - 1 
        i = 0
        vowels = { 
        'a': "Vowel", 
        'e': "Vowel", 
        'i': "Vowel", 
        'o': "Vowel", 
        'u': "Vowel", 
        'A': "Vowel", 
        'E': "Vowel", 
        'I': "Vowel", 
        'O': "Vowel", 
        'U': "Vowel"
    } 
        while pt1 <= pt2 and i < len(strList):
            if vowels.get(strList[pt1], "notVowle") == "Vowel" and vowels.get(strList[pt2], "notVowle") != "Vowel":
                pt2 -=1
            elif vowels.get(strList[pt1], "notVowle") != "Vowel" and vowels.get(strList[pt2], "notVowle") == "Vowel":
                pt1 += 1

            elif vowels.get(strList[pt1], "notVowle") != "Vowel" and vowels.get(strList[pt2], "notVowle") != "Vowel":
                pt2 -=1
                pt1 +=1
            elif vowels.get(strList[pt1], "notVowle") == "Vowel" and vowels.get(strList[pt2], "notVowle") == "Vowel":
                strList[pt1], strList[pt2] = strList[pt2], strList[pt1]
                pt2 -=1
                pt1 +=1
            i += 1
        return ''.join(map(str, strList))
