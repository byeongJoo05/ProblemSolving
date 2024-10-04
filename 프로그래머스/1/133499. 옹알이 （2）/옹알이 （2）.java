import java.util.*;

// 연속된 발음은 안됨.
// 근데 같은 단어를 n번 이상 발음은 가능 -> yeayaye
class Solution {
    public int solution(String[] babbling) {
        List<String> words= List.of("aya", "ye", "woo", "ma");
        int answer = 0;
        
        for (String bab : babbling) {
            boolean isTwiceWord = false;
            for (String word : words) {
                if (bab.contains(word+word)) {
                    isTwiceWord = true;
                    break;
                }
                
                bab = bab.replaceAll(word, " ");
            }
            
            if (isTwiceWord) continue;
            if (bab.trim().length() == 0) answer++;
        }
        
        return answer;
    }
}