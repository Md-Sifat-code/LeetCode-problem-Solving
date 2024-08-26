class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] daysInMonth = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String startDate = arriveAlice.compareTo(arriveBob) > 0 ? arriveAlice : arriveBob;
        String endDate = leaveAlice.compareTo(leaveBob) < 0 ? leaveAlice : leaveBob;
        if(startDate.compareTo(endDate) > 0) {
            return 0;
        }
        int startMonth = Integer.parseInt(startDate.substring(0, 2));
        int startDay = Integer.parseInt(startDate.substring(3));
        int endMonth = Integer.parseInt(endDate.substring(0, 2));
        int endDay = Integer.parseInt(endDate.substring(3));
        
        if(startMonth == endMonth) {
            return endDay - startDay + 1;
        } else { 
            int daysSpentTogether = daysInMonth[startMonth - 1] - startDay;
            for(int month = startMonth + 1; month < endMonth; month++) {
                daysSpentTogether += daysInMonth[month - 1];
            }
            daysSpentTogether += endDay + 1;
            return daysSpentTogether;
        }
    }
}