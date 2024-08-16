class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def bubblesort(heights, names):
            unsorted_until_index = len(heights) - 1
            sorted = False
            while not sorted:
                sorted = True
                for i in range(unsorted_until_index):
                    if heights[i] < heights[i+1]:
                        sorted = False
                        heights[i], heights[i+1] = heights[i+1], heights[i]
                        names[i], names[i+1] = names[i+1], names[i]
                unsorted_until_index = unsorted_until_index - 1
            return names
        return bubblesort(heights, names)