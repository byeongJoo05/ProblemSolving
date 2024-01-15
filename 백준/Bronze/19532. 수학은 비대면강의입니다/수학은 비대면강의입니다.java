import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader stringBuffer = new BufferedReader(new InputStreamReader(System.in));
		String[] strings = stringBuffer.readLine().split(" ");
		int[] nums = new int[strings.length];

		for (int i = 0 ; i < strings.length; i++) {
			nums[i] = Integer.parseInt(strings[i]);
		}

		int a = nums[0];
		int b = nums[1];
		int c = nums[2];
		int d = nums[3];
		int e = nums[4];
		int f = nums[5];

		for (int x = -999 ; x <= 999 ; x++) {
			for (int y = -999 ; y <= 999 ; y ++) {
				if (a*x + b*y == c) {
					if (d*x + e*y == f) {
						System.out.println(x + " " + y);
						System.exit(0);
					}
				}
			}
		}
	}
}
