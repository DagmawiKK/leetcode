class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        checked = set()
        result = set()
        
        for i in range(0, len(s)):
            if s[i:i+10] not in checked:
                checked.add(s[i:i+10])
            else:
                result.add(s[i:i+10])
        
        return list(result)