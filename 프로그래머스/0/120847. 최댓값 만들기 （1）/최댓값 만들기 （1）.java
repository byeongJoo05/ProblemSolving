class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        for (int i = 1; i < numbers.length; i++) {
            for (int j = 0; j < i; j++) {
                int cmp = numbers[i] * numbers[j];
                if (answer < cmp) {
                    answer = cmp;
                }
            }
        }
        return answer;
    }
}