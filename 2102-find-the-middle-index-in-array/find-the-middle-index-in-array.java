class Solution {
    public int findMiddleIndex(int[] nums) {
        int total = Arrays.stream(nums).sum();
        int sumleft = 0;
        for(int l = 0; l < nums.length; l++) {
            if (sumleft != total - sumleft - nums[l]) {
                sumleft += nums[l];
            }
            else {
                return l;
            }
        }
        return -1;
    }
}