package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ10804 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] a = new int[20];
		for (int i = 0 ; i < 20; i++) {
			a[i] = i+1;
		}

		for (int i = 0; i < 10; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int start = Integer.parseInt(st.nextToken()) - 1;
			int end = Integer.parseInt(st.nextToken()) - 1;

			for (; end >= start ; end--) {
				int cmp = a[end];
				a[end] = a[start];
				a[start] = cmp;
				start++;
			}
		}

		StringBuilder st = new StringBuilder();

		for (int i : a) {
			st.append(i).append(" ");
		}

		System.out.println(st);
	}
}
