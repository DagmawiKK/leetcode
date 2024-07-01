class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict = {}
        j = 0
        list = s.split(" ")
        if len(pattern) != len(list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict.keys() and list[j] not in dict.values():
                dict[pattern[i]] = list[j]
                j += 1
            else:
                if dict.get(pattern[i]) != list[j]:
                    return False
                else:
                    j += 1
        print(dict)
        return True