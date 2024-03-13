import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		Integer[] a = new Integer[n];
		int[] b = new int[n];
		Map<Integer, Integer> b_priority = new HashMap<>();
		int answer = 0;

		StringTokenizer a_token = new StringTokenizer(br.readLine(), " ");
		StringTokenizer b_token = new StringTokenizer(br.readLine(), " ");

		for (int i=0; i < n; i++) {
			a[i] = Integer.parseInt(a_token.nextToken());
			b[i] = Integer.parseInt(b_token.nextToken());
		}

		Arrays.sort(a, Comparator.reverseOrder());
		
		int[] b_sort = Arrays.stream(b)
			.sorted()
			.toArray();
		
		for (int i=0; i < n; i++) {
			b_priority.put(i, b_sort[i]);
		}

		for (int i=0 ;i<n; i++) {
			answer += (a[i] * b_priority.get(i));
		}

		System.out.println(answer);
	}
}
