class Solution {
    boolean solution(String s) {
        boolean answer = true;

        char[] c = s.toLowerCase().toCharArray();
        int p_count = 0;
        int y_count = 0;
        
        for (char c1 : c) {
            if ('p' == c1) {
                p_count++;
            } else if ('y' == c1) {
                y_count++;
            }
        }
        
            System.out.println(p_count);
            System.out.println(y_count);
        if (p_count != y_count) {
            answer = false; 
        }
        
        return answer;
    }
}