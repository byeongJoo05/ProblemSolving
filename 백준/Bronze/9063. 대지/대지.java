import java.io.IOException;
import java.util.*;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        solution();
    }

    private static void solution() throws IOException {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] positions = new int[n][2];
        if (n == 1) {
            System.out.println(0);
            System.exit(0);
        }

        scanner.nextLine();
        for (int i = 0; i < n; i++) {
            int[] position = Stream.of(scanner.nextLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            positions[i][0] = position[0];
            positions[i][1] = position[1];
        }

        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;

        for (int[] position : positions) {
            if (minX > position[0]) minX = position[0];
            if (maxX < position[0]) maxX = position[0];
            if (minY > position[1]) minY = position[1];
            if (maxY < position[1]) maxY = position[1];
        }

        System.out.println((maxX-minX) * (maxY-minY));
    }
}
