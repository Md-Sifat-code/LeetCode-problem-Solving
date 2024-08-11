class Solution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        
        int n = nums.length;
        int[] arr = new int[n];
        int index = 0;
        for (int i = 0; i < n; i += 2) {

            arr[index++] = nums[i + 1];
            arr[index++] = nums[i];
        }
        
        return arr;
    }
}