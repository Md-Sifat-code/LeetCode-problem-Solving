class Solution {
    private String common(String s1, String s2){
        int n = Math.min(s1.length(),s2.length());
        StringBuilder sb =new StringBuilder();
        for(int i = 0; i<n;i++){
            if(s1.charAt(i) == s2.charAt(i)){
                sb.append(s1.charAt(i));
            }
            else{
                break;
            }
            
        }
        return sb.toString();
    }
    public String longestCommonPrefix(String[] strs) {
        String result = strs[0];
        int x =strs.length;
        if (strs == null || strs.length == 0) {
            return "";
        }
        for(int i =1;i<x;i++){
            result = common(result, strs[i]);
            if(result.isEmpty()){
                break;
            }
        }
        return result;
    }
}