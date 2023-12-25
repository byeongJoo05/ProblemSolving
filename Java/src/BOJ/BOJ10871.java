package BOJ;

import java.io.*;
import java.util.*;

public class BOJ10871 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");

		int n = Integer.parseInt(input[0]);
		int x = Integer.parseInt(input[1]);

		List<Integer> list = new ArrayList<>();

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int a = Integer.parseInt(st.nextToken());
			if (a < x) {
				list.add(a);
			}
		}

		StringBuilder sb = new StringBuilder();
		for (Integer result : list) {
			sb.append(result)
				.append(" ");
		}
		System.out.println(sb);
	}
}
