import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int answer = 0;


		if (n < 100) {
			System.out.println(n);
			System.exit(0);
		} else {
			answer = 99;
			for (int i = 100; i <= n; i++) {
				int hundred = i / 100;
				int ten = (i / 10) % 10;
				int one = i % 10;

				if ((hundred - ten) == (ten - one)) {
					answer++;
				}
			}
		}

		System.out.println(answer);
	}
}