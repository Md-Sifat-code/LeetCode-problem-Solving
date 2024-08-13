class Solution {
    public int scoreOfString(String s) {
        int x = 0;
        for(int i =1; i<s.length();i++){
            x += Math.abs(s.charAt(i)-s.charAt(i-1));
        }
        return x;
    }
}