class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        arr = []
        result = []
        
        for i in range(0, len(s)):
            current_seq = s[i:i+10]
            k = i+1
            arr.append(current_seq)
        count = Counter(arr)
        for i in count:
            if count[i] > 1:
                result.append(i)
        return result