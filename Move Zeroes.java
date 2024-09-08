class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int y = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[y] = nums[i];
                y++;
            }
        }
        for (int i = y; i < n; i++) {
            nums[i] = 0;
        }
    }
}
