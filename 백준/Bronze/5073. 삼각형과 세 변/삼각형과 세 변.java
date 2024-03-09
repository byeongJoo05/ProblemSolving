import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int[] nums;


	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			String[] inputs = br.readLine().split(" ");

			nums = Arrays.stream(inputs)
				.mapToInt(Integer::parseInt)
				.toArray();

			if (Arrays.stream(nums).sum() == 0) {
				System.exit(0);
			}

			Arrays.sort(nums);

			if(nums[2] >= nums[0] + nums[1]) {
				System.out.println("Invalid");
			}else if(nums[0] == nums[1] && nums[1] == nums[2]) {
				System.out.println("Equilateral");
			}else if(nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2]) {
				System.out.println("Isosceles");
			}else {
				System.out.println("Scalene");
			}
		}
	}
}
