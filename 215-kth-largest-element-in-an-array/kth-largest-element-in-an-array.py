class Solution:
    def findKthLargest( nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k - 1]

    with open('user.out', 'w') as f:
        inputs = sys.stdin.read().splitlines()
        for i in range(0, len(inputs), 2):
            nums = json.loads(inputs[i])
            k = int(inputs[i + 1])
            result = findKthLargest(nums, k)
            print(result, file=f)
    exit()