class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        index = 0
        for char in count:
            if count[char] == 1:
                return index
            index += 1 
        return -1