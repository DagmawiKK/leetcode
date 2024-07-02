class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        for char in s[::-1]:
            s.pop(i)
            s.insert(i, char)
            i +=1