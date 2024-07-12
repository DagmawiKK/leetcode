class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i], names[i]) for i in range(len(names))]
        
        n = len(people)
        for i in range(n):
            for j in range(0, n-i-1):
                if people[j][0] < people[j+1][0]:
                    people[j], people[j+1] = people[j+1], people[j]
        
        sorted_names = [person[1] for person in people]
        
        return sorted_names
