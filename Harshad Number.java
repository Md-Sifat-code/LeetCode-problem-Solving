class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sumOfDigits = 0;
        int temp = x;
        while (temp > 0) {
            sumOfDigits += temp % 10;
            temp /= 10;
        }
        if (x % sumOfDigits == 0) {
            return sumOfDigits;
        } else {
            return -1;
        }
    }
}