public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if(n==1){
            return n;
        }
        int badVersion =1;
        int start =1;
        int end = n;
        while(start <= end){
            int mid = start +(end-start)/2;
            if(isBadVersion(mid)){
                badVersion = mid;
                end = mid-1;
            }else{
                start = mid +1;
            }
        }
        return badVersion;
    }
}