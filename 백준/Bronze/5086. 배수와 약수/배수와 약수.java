import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int[] values = Stream.of(scanner.nextLine().split(" "))
                             .mapToInt(Integer::parseInt)
                             .toArray();
            int a = values[0];
            int b = values[1];

            if (a == 0) break;
            
            if (b % a == 0) {
                System.out.println("factor");
            } else if (a % b == 0) {
                System.out.println("multiple");
            } else {
                System.out.println("neither");
            }
        }
    }
}
