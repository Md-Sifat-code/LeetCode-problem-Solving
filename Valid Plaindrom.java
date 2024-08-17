class Solution {
    public boolean isPalindrome(String s) {
        int n= s.length();
        int i= 0;
        int j= n-1;
        while(i <= j){
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                i++;
            }
            
            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                j--;
            }
            int c1= Character.toLowerCase(s.charAt(i));
            int c2= Character.toLowerCase(s.charAt(j));
            if(c1 != c2){
                return false;
            }
            i++; j--;
        }
        return true;
    }
}