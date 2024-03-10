import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {


	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] split = br.readLine().split(" ");

		int[] nums = Arrays.stream(split)
			.mapToInt(Integer::parseInt)
			.toArray();

		Arrays.sort(nums);

		System.out.println(nums[1]);
	}
}