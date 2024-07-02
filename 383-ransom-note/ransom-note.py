class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for item in ransomNote:
            if item in magazine:
                magazine.remove(item)
                continue
            else:
                return False
        return True