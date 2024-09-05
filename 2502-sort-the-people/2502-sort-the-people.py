class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def bubble(heights, names):
            unsorted_until_index = len(heights) - 1
            sortedd = False
            while not sortedd:
                sortedd = True
                for i in range(unsorted_until_index):
                    if heights[i] < heights[i+1]:
                        sortedd = False
                        heights[i], heights[i + 1] = heights[i + 1], heights[i]
                        names[i], names[i+1] = names[i+1], names[i]
                unsorted_until_index -= 1
            return names
        return bubble(heights, names)