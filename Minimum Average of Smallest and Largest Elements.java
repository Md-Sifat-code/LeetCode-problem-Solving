class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        double minElement = Double.MAX_VALUE;
        int i = 0;
        int j = nums.length-1;
        double avg;
        while(i < j){
            avg = ((double) nums[i] + nums[j])/2;
            if(avg < minElement){
                minElement = avg;
            }
            i++;
            j--;
        }
        return minElement;
    }
}