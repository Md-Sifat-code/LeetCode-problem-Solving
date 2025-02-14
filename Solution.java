public public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int  start =1;
        int end =n;
        if(guess(n) == 0){
            return n;
        }
           
            while(start <=end){
                 int mid = start + (end-start)/2;
                if(guess(mid)==0){
                    return mid;
                }else if(guess(mid) == 1){
                    start = mid+1;
                    end =n;
                }else{
                    start = start;
                    end = mid -1;
                    
                }
            }
        
        return -1;
    }
} {
    
}
