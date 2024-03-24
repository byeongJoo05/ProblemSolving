import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> setWears = new HashMap<>();

        int answer = 1;

        for (String[] clothe : clothes) {
            String clothKind = clothe[1];

            if (!setWears.containsKey(clothKind)) {
                setWears.put(clothKind, 1);
            } else{
                setWears.put(clothKind, setWears.get(clothKind)+1);
            }
            
        }
        
        for (String key : setWears.keySet()) {
            answer *= (setWears.get(key) + 1); // 안 입는 경우
        }
        
        answer -= 1; // all 안 입는 경우 빼기
        
        return answer;
    }
}