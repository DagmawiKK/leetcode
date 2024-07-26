class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <=10:
            return []
        checked = set()
        result = set()
        
        for i in range(len(s)-9):
            if s[i:i+10] not in checked:
                checked.add(s[i:i+10])
            else:
                result.add(s[i:i+10])
        
        return list(result)