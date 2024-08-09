class Solution {
    public int maximumWealth(int[][] accounts) {
        int n = accounts.length;
        
        int x = accounts[0].length;
        int output = 0;
        for(int i=0;i<n;i++){
            int temp =0;
            for(int j = 0;j<x;j++){
                temp += accounts[i][j];

            }
            if(temp>output){
                output = temp;
            }

        }
        return output;
    }
}    

