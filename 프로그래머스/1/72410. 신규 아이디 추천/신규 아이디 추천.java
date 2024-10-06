import java.util.*;

class Solution {
    public String solution(String new_id) {
        if (new_id.isEmpty()) return "aaa";
        
        List<Character> exp = List.of('-','_','.');
        StringBuilder answer = new StringBuilder();
        
        new_id = new_id.toLowerCase();
        char[] new_id_chr = new_id.toCharArray();
        int start = 0; 
        int end = new_id_chr.length;
        if (new_id_chr[0] == '.') start += 1;
        if (new_id_chr[new_id_chr.length-1] == '.') end -= 1;
        
        boolean isDot = false;
        for (int i = start; i < end; i++) {
            char chr = new_id_chr[i];
            if (chr == '.') {
                if (isDot) continue;
                isDot = true;
            } else isDot = false;
            
            if (!Character.isAlphabetic(chr) && !Character.isDigit(chr) && !exp.contains(chr)) {
                continue;
            }
            answer.append(chr);
        }
        
        String result = answer.toString();
        if (result.isEmpty()) return "aaa";
        
        while (result.contains("..")) {
            result = result.replace("..", ".");
        }
        
        if (result.length() > 0 && result.charAt(0) == '.') {
            if (result.length() == 1) return "aaa";
            result = result.substring(1);
        }
        
        if (result.length() > 0 && result.charAt(result.length() - 1) == '.') {
            result = result.substring(0, result.length() - 1);
        }
        
        if (result.length() >= 16) {
            result = result.substring(0, 15);
            if (result.length() > 0 && result.charAt(result.length() - 1) == '.') {
                result = result.substring(0, result.length() - 1);
            }
        }
        
        while (result.length() < 3) {
            result += result.charAt(result.length() - 1);
        }
        
        return result;
    }
}
