class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int x = 0;
            for (int j = 0; j < n; j++) {
                if (nums[i] == nums[j]) {
                    x++;
                }
            }
            if (x > n / 2) {
                return nums[i];
            }
        }
        return -1;
    }
}