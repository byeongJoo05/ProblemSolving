import java.util.*;

// aaaaa -> 5, aaaae -> 10
// aaaa -> 4, aaae -> 11, aaai -> 17, aaao -> 23, aaau -> 29
// aaa - > 3, aae -> 34
// aa -> 2, ae -> 158
// (i-1) + 5^i
// 5번째 1, 4번째 6, 3번째 31, 2번째 156, 1번째 781
class Solution {
    public int solution(String word) {
        int answer = word.length();
        
        // 초기 a는 1씩 나오게끔 해야되는데..
        int[] weight = {781, 156, 31, 6 , 1};
        String alpha = "AEIOU";
        
        for (int i = 0; i < word.length(); i++) {
            answer += weight[i] * alpha.indexOf(word.charAt(i));
        }
        
        return answer;
    }
}