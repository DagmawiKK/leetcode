class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums=list(map(lambda char:ord(char)-97,s))
        base = [0] * (len(nums) + 1)
        for query in shifts:
            start,end,dirc =query
            if dirc == 1:
                base[start]+=1
                if end + 1 < len(base):
                    base[end+1] -= 1
            else:
                base[start]-=1
                if end + 1 < len(base):
                    base[end+1] += 1
        base = list(accumulate(base))
        for i in range(len(nums)):
            nums[i]+=base[i]
            nums[i]=chr((nums[i]%26)+97)
        return "".join(nums)



             
