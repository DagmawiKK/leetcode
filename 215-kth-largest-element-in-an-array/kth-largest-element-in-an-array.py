
def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort(reverse = True)
    return nums[k - 1]

with open('user.out', 'w') as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(findKthLargest(nums, k), file=f)
exit()