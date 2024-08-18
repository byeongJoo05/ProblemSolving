import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] values = Stream.of(scanner.nextLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
        int a = values[0];
        int b = values[1];
        List<Integer> arr = new ArrayList<>();

        for (int i = 1; i <= a; i++) {
            if (a % i == 0) arr.add(i);
        }

        if (arr.isEmpty() || arr.size() < b) {
            System.out.println(0);
        } else {
            System.out.println(arr.get(b-1));
        }
    }
}
