class Solution {
    private int getSquareSum(int n)
    {
        int currSum = 0;
        while(n != 0)
        {
            int remainder = (n % 10);
            currSum += remainder * remainder;
            n /= 10;
        }
        return currSum;

    }

    public boolean isHappy(int n) {
        int slow = getSquareSum(n);
        int fast = getSquareSum(getSquareSum(n));
        while((slow != fast) && (fast != 1))
        {
            slow = getSquareSum(slow);
            fast = getSquareSum(getSquareSum(fast));
        }

        return fast == 1;
    }
}