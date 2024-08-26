class Solution {
    public int smallestEvenMultiple(int n) {
        int x =0;
        for(int i = 0; i<= n*2; i++){
            if(i%2==0 && i%n==0){
                x+=i;
            }
            if(x>0){
                break;
            }
        }
        return x;
        
    }
}
