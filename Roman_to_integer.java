class Solution {
    private int translate(char c) {
        switch(c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    
    public int romanToInt(String s) {
        int sum = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int current = translate(s.charAt(i));
            
            if (i < n - 1 && current < translate(s.charAt(i + 1))) {
                // Subtractive case
                sum -= current;
            } else {
                // Additive case
                sum += current;
            }
        }

        return sum;
    }
}
