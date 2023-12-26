package BOJ;

import java.util.*;
import java.io.*;

public class BOJ10773 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		Stack<Integer> stack = new Stack<>();

		int n = Integer.parseInt(br.readLine());
		int sum = 0;

		for (int i = 0 ; i < n; i++) {
			int a = Integer.parseInt(br.readLine());

			if (a > 0) {
				stack.push(a);
			}
			else {
				stack.pop();
			}
		}

		if (stack.isEmpty()) {
			System.out.println("0");
			System.exit(0);
		}

		for (Integer a : stack) {
			sum += a;
		}

		System.out.println(sum);
	}
}
