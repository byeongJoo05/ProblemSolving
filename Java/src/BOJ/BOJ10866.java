package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class BOJ10866 {
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(reader.readLine());
		Deque<Integer> deque = new ArrayDeque<>();

		for (int i = 0; i < n; i++) {
			StringTokenizer token = new StringTokenizer(reader.readLine());
			String mod = token.nextToken();

			if (mod.equals("push_back")) {
				int num = Integer.parseInt(token.nextToken());

				deque.addLast(num);
			} else if (mod.equals("push_front")) {
				int num = Integer.parseInt(token.nextToken());
				deque.addFirst(num);
			} else if (mod.equals("front")) {

				if (deque.isEmpty()) {
					System.out.println("-1");
					continue;
				}
				System.out.println(deque.getFirst());
			} else if (mod.equals("back")) {

				if (deque.isEmpty()) {
					System.out.println("-1");
					continue;
				}
				System.out.println(deque.getLast());
			} else if (mod.equals("pop_front")) {

				if (deque.isEmpty()) {
					System.out.println("-1");
					continue;
				}
				System.out.println(deque.removeFirst());
			} else if (mod.equals("pop_back")) {

				if (deque.isEmpty()) {
					System.out.println("-1");
					continue;
				}
				System.out.println(deque.removeLast());
			} else if (mod.equals("size")) {
				System.out.println(deque.size());
			} else if (mod.equals("empty")) {

				if (deque.isEmpty()) {
					System.out.println("1");
					continue;
				}
				System.out.println("0");
			}
		}
	}
}
