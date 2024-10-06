import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Data> queue = new LinkedList<>();
        
        for (int i = 0; i < priorities.length ; i++) {
            Data data = new Data(i, priorities[i]);
            queue.offer(data);
        }
        
        Arrays.sort(priorities);
        int count = 1;
        while (!queue.isEmpty()) {
            Data data = queue.poll();
            
            // 높은 우선순위 데이터 먼저 검증
            while (data.priority != priorities[priorities.length - count]) {
                queue.offer(data);
                data = queue.poll();
            }
            
            // 동등한 순위일 경우 poll을 순차대로 시키면서 location 확인
            if (data.idx == location) break;
            
            // 우선순위 && 동등 순위 확인 횟수
            count++;
        }
        
        return count;
    }
}

class Data {
    int idx;
    int priority;
    
    public Data (int idx, int priority) {
        this.idx = idx;
        this.priority = priority;
    }
}