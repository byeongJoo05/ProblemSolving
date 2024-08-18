import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int n = scanner.nextInt();
            if (n == -1) break;
            StringBuilder sb = new StringBuilder();
            List<Integer> nums = new ArrayList<>();

            for (int i = 1; i < n; i++) {
                if (n%i == 0) nums.add(i);
            }

            if (n == nums.stream().mapToInt(i->i).sum()) {
                sb.append(n + " = ");

                for (int i = 0; i < nums.size()-1; i ++) {
                    sb.append(nums.get(i) + " + ");
                }
                sb.append(nums.get(nums.size()-1));
                System.out.println(sb);
            } else {
                System.out.println(String.format("%d is NOT perfect.", n));
            }
        }
    }
}
