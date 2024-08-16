class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) -1
        returnSum = skill[left] * skill[right]
        left += 1
        right -= 1
        while left < right:
            if (skill[left - 1] + skill[right+1]) == (skill[left] + skill[right]):
                # result.append((skill[left], skill[right]))
                returnSum += (skill[left] * skill[right])
            else:
                return -1
            right -= 1
            left += 1
        return returnSum
