package BOJ;

import java.io.*;
import java.util.*;

public class BOJ10828 {

	public static void main(String[] args) throws IOException {
		Stack<Integer> stack = new Stack<>();

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		for (int i =0 ; i < n ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String mod = st.nextToken();

			if (mod.equals("push")) {
				int p = Integer.parseInt(st.nextToken());
				stack.push(p);
			} else if (mod.equals("pop")) {
				if (stack.isEmpty()) {
					System.out.println("-1");
				} else {
					System.out.println(stack.pop());
				}
			} else if (mod.equals("size")) {
				System.out.println(stack.size());
			} else if (mod.equals("empty")) {
				if (stack.isEmpty()) {
					System.out.println("1");
				} else {
					System.out.println("0");
				}
			} else if (mod.equals("top")) {
				if (stack.isEmpty()) {
					System.out.println("-1");
				} else
					System.out.println(stack.peek());
			}
		}
	}
}
