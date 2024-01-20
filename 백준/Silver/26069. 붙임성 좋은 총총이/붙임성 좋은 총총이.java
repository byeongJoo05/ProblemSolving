import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(bufferedReader.readLine());
		Set<String> rainbow = new HashSet<>();
		for (int i = 0; i < n; i++) {
			String[] members = bufferedReader.readLine().split(" ");

			boolean containedChongChong = Arrays.asList(members).contains("ChongChong");

			if (containedChongChong) {
				rainbow.addAll(Arrays.asList(members));
				continue;
			}

			if (rainbow.contains(members[0])) {
				rainbow.add(members[1]);
			} else if (rainbow.contains(members[1])) {
				rainbow.add(members[0]);
			}
		}

		System.out.println(rainbow.size());
	}
}
