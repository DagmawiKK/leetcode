class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()

        def sort_str(my_str):
            return int(my_str[-1])
        lst.sort(key=sort_str)
        string = ""
        for i in lst:
            string = string + i[:len(i) - 1] + " "
        return string.strip()