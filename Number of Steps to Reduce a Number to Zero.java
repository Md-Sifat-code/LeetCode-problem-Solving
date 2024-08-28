class Solution {
    public:
        int numberOfSteps(int num) {
            int x = num;
            int count = 0;
            for(int i = 0; x > 0; i++){  // Fix: Changed x < 1 to x > 0
                if(x % 2 == 0){
                    x = x / 2;
                } else {
                    x = x - 1;
                }
                count++;
            }
            return count;
        }
    };