class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;  // Handle cases where k >= n
        int[] output = new int[n];

        // Copy elements to the correct position in the output array
        for(int i = 0; i < n; i++) {
            output[(i + k) % n] = nums[i];
        }

        // Copy the rotated array back into the original array
        for(int i = 0; i < n; i++) {
            nums[i] = output[i];
        }
    }
}
