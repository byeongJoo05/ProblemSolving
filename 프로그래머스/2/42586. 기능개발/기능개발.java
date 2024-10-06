// 7, 3, 9

// 5, 10, 1, 1, 20, 1
import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int day = (int) Math.ceil((double)(100-progresses[i]) / speeds[i]);
            queue.offer(day);
        }
        
        int count = 1;
        int big = queue.poll();
        
        if (queue.isEmpty()) {
            answer.add(count);
            return answer;
        }
        
        while (!queue.isEmpty()) {
            int tmp = queue.poll();
            
            if (big >= tmp) count++;
            else {
                answer.add(count);
                big = tmp;
                count = 1;
            }
        }
        answer.add(count);
        
        return answer;
    }
}