class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) return 0;

        int low = prices[0];  // Initialize low with the first price
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            // Update the minimum price encountered so far
            if (prices[i] < low) {
                low = prices[i];
            }
            // Calculate the profit if sold at the current price and update maxProfit if it's higher
            else {
                maxProfit = Math.max(maxProfit, prices[i] - low);
            }
        }

        return maxProfit;
    }
}