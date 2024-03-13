import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		Map<String, Integer> books = new TreeMap<>();
		for (int i = 0 ; i < n; i++) {
			String title = br.readLine();

			if (!books.containsKey(title)) {
				books.put(title, 1);
			} else{
				books.put(title, books.get(title)+1);
			}
		}

		List<Integer> list = new ArrayList<>(books.values());
		list.sort(Collections.reverseOrder());
		int max = list.get(0);

		for (Map.Entry<String, Integer> entry : books.entrySet()) {
			if (entry.getValue() == max) {
				System.out.println(entry.getKey());
				break;
			}
		}
	}
}
