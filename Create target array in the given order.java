class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
         int[] target = new int[nums.length];
        for (int i = 0; i < target.length; i++) {
            target[i] = Integer.MAX_VALUE;
        }
        
        for (int i = 0; i < nums.length; i++) {
            int insertIndex = index[i];
            
            if (target[insertIndex] != Integer.MAX_VALUE) {
                for (int j = target.length - 1; j > insertIndex; j--) {
                    target[j] = target[j - 1];
                }
            }
            target[insertIndex] = nums[i];
        }
        
        return target;
        
    }
}