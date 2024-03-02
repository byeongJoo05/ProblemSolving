import java.util.*;
import java.util.Arrays;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for (int i=0; i< discount.length - 9; i++) {
            String[] rangedDc = Arrays.copyOfRange(discount, i, i+10);
            List<String> list = Arrays.asList(rangedDc);
            boolean flag = true;
            for (int j = 0; j < want.length ; j ++) {
                if (Collections.frequency(list, want[j]) != number[j]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                answer += 1;
            }
        }
        return answer;
    }
}