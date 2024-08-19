class Solution {
    public int averageValue(int[] nums) {
        int x = 0;
        int count = 0;

        for (int num : nums) {

            if (num % 6 == 0) {
                x += num;
                count++;
            }
        }

        if (count != 0) {
            return x / count;
        } else {
            return 0;
        }
    }
}
