import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        List<Integer> LEFT_KEY = List.of(1, 4, 7);
        List<Integer> RIGHT_KEY = List.of(3, 6, 9);

        int[] left_cur = {3, 0};
        int[] right_cur = {3, 2};

        StringBuilder answer = new StringBuilder();

        for (int number : numbers) {
            if (LEFT_KEY.contains(number)) {
                answer.append("L");
                left_cur = getIndex(number);
            } else if (RIGHT_KEY.contains(number)) {
                answer.append("R");
                right_cur = getIndex(number);
            } else {
                int[] numXY = getIndex(number);
                int l_distance = Math.abs(numXY[0] - left_cur[0]) + Math.abs(numXY[1] - left_cur[1]);
                int r_distance = Math.abs(numXY[0] - right_cur[0]) + Math.abs(numXY[1] - right_cur[1]);

                if (l_distance < r_distance) {
                    answer.append("L");
                    left_cur = getIndex(number);
                } else if (r_distance < l_distance) {
                    answer.append("R");
                    right_cur = getIndex(number);
                } else {
                    if ("left".equals(hand)) {
                        answer.append("L");
                        left_cur = getIndex(number);
                    } else {
                        answer.append("R");
                        right_cur = getIndex(number);
                    }
                }
            }
        }
        return answer.toString();
    }

    public int[] getIndex(int num) {
        if (num == 0) {
            return new int[]{3, 1};
        }
        int row = (num - 1) / 3;
        int col = (num - 1) % 3;
        return new int[]{row, col};
    }
}