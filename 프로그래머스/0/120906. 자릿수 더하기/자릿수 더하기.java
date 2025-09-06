import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String nString = n+"";
        
        for (int i = 0; i < nString.length(); i++) {
            answer += Character.getNumericValue(nString.charAt(i));
        }
        
        return answer;
    }
}