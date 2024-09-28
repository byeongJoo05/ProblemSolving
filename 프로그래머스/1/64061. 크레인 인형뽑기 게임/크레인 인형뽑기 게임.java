import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int n = board.length;
        int answer = 0;

        for (int move : moves) {
            int idx = move - 1;

            for (int i = 0; i < n; i++) {
                int pick = board[i][idx];
                if (pick == 0) continue;

                if (!stack.isEmpty() && stack.peek() == pick) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(pick);
                }

                board[i][idx] = 0;
                break;
            }
        }
        return answer;
    }
}