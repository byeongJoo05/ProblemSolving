package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * push 순서는 오름차 순이여야 하니 가장 윗단 top이 수열 중 가장 큰 수여야 한다.
 */
public class BOJ1874 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		Stack<Integer> stack = new Stack<>();
		StringBuilder sb = new StringBuilder();

		int seq = 0; // top과 비교할 시퀀스

		for (int i = 0 ; i < n; i++) {
			int num = Integer.parseInt(br.readLine());

			if (num > seq) {
				for (int j = seq + 1 ; j <= num ; j++) {
					stack.push(j);
					sb.append("+").append("\n");
					seq++;
				}
			} else if (num < stack.peek() && !stack.isEmpty()) {
				while (num < stack.peek()) {
					stack.pop();
					sb.append("-").append("\n");
				}

				if (num == stack.peek()) {
					System.out.println("NO");
					System.exit(0);
				}
			}

			stack.pop();
			sb.append("-").append("\n");
		}

		System.out.println(sb);
	}
}
