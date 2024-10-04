import java.util.*;
// 1번 지표 - RT, 2번 - CF, 3번 - JM, 4번 - AN
// survey[0] -> 비동의, survey[1] -> 동의

// choices 1~3 비동의, 4 모름, 5~7 동의
class Solution {
    Map<Character, Integer> first = new HashMap<>();
    Map<Character, Integer> second = new HashMap<>();
    Map<Character, Integer> third = new HashMap<>();
    Map<Character, Integer> forth = new HashMap<>();
    
    public String solution(String[] surveys, int[] choices) {
        String answer = "";
        // Map<Character, Integer> first = new HashMap<>();
        first.put('R', 0); first.put('T', 0);
        // Map<Character, Integer> second = new HashMap<>();
        second.put('C', 0); second.put('F', 0);
        // Map<Character, Integer> third = new HashMap<>();
        third.put('J', 0); third.put('M', 0);
        // Map<Character, Integer> forth = new HashMap<>();
        forth.put('A', 0); forth.put('N', 0);
        
        for (int i = 0; i < surveys.length; i++) {
            int choice = choices[i];
            if (choice == 4) continue;
            String survey = surveys[i];
            
            // 포인트
            int point = choose(choice);
            
            // 좌측 우측 선택.
            char section = survey.charAt(leftOrRight(choice));
            if (survey.contains("R")) {
                first.replace(section, first.get(section) + point);
            } else if (survey.contains("C")) {
                second.replace(section, second.get(section) + point);
            } else if (survey.contains("J")) {
                third.replace(section, third.get(section) + point);
            } else {
                forth.replace(section, forth.get(section) + point);
            }
        }
        
        answer += appendResult(first);
        answer += appendResult(second);
        answer += appendResult(third);
        answer += appendResult(forth);
        
        return answer;
    }
    
    public String appendResult(Map<Character, Integer> map) {
        List<Map.Entry<Character, Integer>> entries = new ArrayList<>(map.entrySet());

        Map.Entry<Character, Integer> firstEntry = entries.get(0);
        Map.Entry<Character, Integer> secondEntry = entries.get(1);

        if (firstEntry.getValue().equals(secondEntry.getValue())) {
            return String.valueOf(firstEntry.getKey());
        } else {
            if (firstEntry.getValue() > secondEntry.getValue()) return String.valueOf(firstEntry.getKey());
            return String.valueOf(secondEntry.getKey());
        }
    }
    
    public int choose (int choice) {
        if (choice == 1 || choice == 7) return 3;
        if (choice == 2 || choice == 6) return 2;
        if (choice == 3 || choice == 5) return 1;
        return 0;
    }
    
    public int leftOrRight (int choice) {
        if (choice >=1 && choice <= 3) return 0;
        return 1;
    }
}