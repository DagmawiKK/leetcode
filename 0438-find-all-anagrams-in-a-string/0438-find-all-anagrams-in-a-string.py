class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        sCounter, pCounter = defaultdict(int), defaultdict(int)

        for i in range(len(p)):
            pCounter[p[i]] += 1
            sCounter[s[i]] += 1 

        res = []
        if sCounter == pCounter:
            res.append(0)


        left = 0 

        for right in range(len(p), len(s)):
            sCounter[s[right]] += 1
            sCounter[s[left]] -= 1 

            if sCounter[s[left]] == 0:
                del sCounter[s[left]]
            left += 1
            

            if sCounter == pCounter:
                res.append(left)


        return res


