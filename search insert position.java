class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        int x = 0;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] == target) {
                return i;
            } else if (i != 0 && nums[i-1] < target && nums[i] > target) {
                return i;
            } else if (i == 0 && target < nums[i]) {
                return 0;
            } else if (i == n-1 && target > nums[i]) {
                return n;
            }
        }
        
        return x;
    }
}