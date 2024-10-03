// Brute Force approch;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max_sum = INT_MIN; // Correctly initialized to the smallest possible value
        for(int st = 0; st < n; st++) {
            int current_sum = 0;
            for(int end = st; end < n; end++) {
                current_sum += nums[end];
                max_sum = max(current_sum, max_sum);
            }
        }
        return max_sum;
    }
};