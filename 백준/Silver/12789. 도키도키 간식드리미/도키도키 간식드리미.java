import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> stack = new Stack<>();

		int n = Integer.parseInt(bufferedReader.readLine());
		String[] data = bufferedReader.readLine().split(" ");
		int[] num = Arrays.stream(data).mapToInt(Integer::parseInt).toArray();
		int cur = 1;
		for (int i = 0; i < n ; i++) {
			if (stack.size() != 0) {
				while (stack.peek() == cur) {
					stack.pop();
					cur++;

					if (stack.size() == 0) {
						break;
					}
				}
			}
			if(num[i] > cur) {
				if (stack.size() != 0) {
					if (stack.peek() < num[i]) {
						System.out.println("Sad");
						System.exit(0);
					}
				}
				stack.push(num[i]);
			} else {
				if (num[i] == cur) {
					cur++;
				}
			}
		}

		if (stack.size() != 0) {
			while (stack.peek() == cur) {
				stack.pop();
				cur++;

				if (stack.size() == 0) {
					break;
				}
			}
		}

		if (stack.size() == 0) {
			System.out.println("Nice");
		} else {
			System.out.println("Sad");
		}
	}
}
