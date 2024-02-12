class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        String target = board[h][w];
        int n = board.length;
        int[] dh = new int[]{0, 1, -1, 0};
        int[] dw = new int[]{1, 0, 0, -1};
        
        for (int i = 0; i < 4; i++) {
            int dx = w+dw[i];
            int dy = h+dh[i];
            
            if (dy >=0 && dx >= 0 && dy < n && dx < n) {
                if (target.equals(board[dy][dx])) answer += 1;
            }
        }
        return answer;
    }
}