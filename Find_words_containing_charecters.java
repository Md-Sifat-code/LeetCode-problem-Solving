class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        int n = words.length;
        List<Integer> output = new ArrayList<>();
        String y;

        for(int i = 0; i<n ; i++){
            y = words[i];
            
            if(y.indexOf(x) != -1){
                output.add(i);
            }
            
        }
        return output;
    }
}