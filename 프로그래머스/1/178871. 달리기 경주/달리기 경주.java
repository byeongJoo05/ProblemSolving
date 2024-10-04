import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        HashMap<String, Integer> ranks = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            ranks.put(players[i], i);
        }
        
        for (String calling : callings) {
            int playerIdx = ranks.get(calling);
            String frontPlayer = players[playerIdx-1];
            
            ranks.replace(frontPlayer, playerIdx);
            ranks.replace(calling, playerIdx-1);
            
            players[playerIdx] = frontPlayer;
            players[playerIdx-1] = calling;
        }
        
        return players;
    }
}