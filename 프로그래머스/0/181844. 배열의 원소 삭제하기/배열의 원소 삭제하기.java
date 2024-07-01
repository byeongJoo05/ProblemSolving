import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int[] delete_list) {
        List<Integer> ans = new ArrayList<>();
        
        for (int i : arr) {
            ans.add(i);
        }
        
        for (int del : delete_list) {
            if (ans.contains(del)) {
                int idx = ans.indexOf(del);

                ans.remove(idx);
            }
        }
        
        return ans;
    }
}