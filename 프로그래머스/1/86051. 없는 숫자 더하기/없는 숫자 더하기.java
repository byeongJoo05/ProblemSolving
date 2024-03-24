import java.util.*;
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        List<Integer> list = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9));
        
        for (int number : numbers) {
            if (list.contains(number)) {
                list.remove(Integer.valueOf(number));
            }
        }

        int sum = list.stream()
                .mapToInt(Integer::intValue)
                .sum();
        
        return sum;
    }
}