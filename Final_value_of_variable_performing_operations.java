class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int temp =0;
        int n = operations.length;
        for(int i = 0; i<n;i++){
            if(operations[i].equals("X++") || operations[i].equals("++X")){
                temp += 1;
            }
            else if(operations[i].equals("X--") || operations[i].equals("--X")){
                temp -= 1;
            }

        }
        return temp;
    }
}