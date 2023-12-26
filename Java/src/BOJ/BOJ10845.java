package BOJ;

import java.util.*;
import java.io.*;

public class BOJ10845 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		Queue<Integer> queue = new LinkedList<>();
		Stack<Integer> stack = new Stack<>();

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String mod = st.nextToken();

			if (mod.equals("push")) {
				String token = st.nextToken();
				queue.add(Integer.parseInt(token));
				stack.add(Integer.parseInt(token));
			} else if (mod.equals("front")) {
				if (queue.isEmpty()) {
					System.out.println("-1");
				} else {
					System.out.println(queue.peek());
				}
			} else if (mod.equals("back")) {
				if (queue.isEmpty()) {
					System.out.println("-1");
				} else {
					System.out.println(stack.peek());
				}
			} else if (mod.equals("size")) {
				System.out.println(queue.size());
			} else if (mod.equals("empty")) {
				if (queue.isEmpty()) {
					System.out.println("1");
					stack.clear();
				} else {
					System.out.println("0");
				}
			} else if (mod.equals("pop")) {
				if (queue.isEmpty()) {
					System.out.println("-1");
				} else {
					System.out.println(queue.poll());
				}
			}
		}
	}
}
