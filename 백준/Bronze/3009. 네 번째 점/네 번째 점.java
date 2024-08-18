import java.io.IOException;
import java.util.*;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        solution();
    }

    private static void solution() throws IOException {
        Scanner scanner = new Scanner(System.in);
        List<int[]> points = new ArrayList<>();
        int x = 0;
        int y = 0;

        for (int i = 0; i < 3; i++) {
            int[] positions = Stream.of(scanner.nextLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            points.add(positions);
        }

        int[] point1 = points.get(0);
        int[] point2 = points.get(1);
        int[] point3 = points.get(2);

        if (point1[0] == point2[0]) {
            x = point3[0];
        } else if (point1[0] == point3[0]) {
            x = point2[0];
        } else if (point2[0] == point3[0]) {
            x = point1[0];
        }

        if (point1[1] == point2[1]) {
            y = point3[1];
        } else if (point1[1] == point3[1]) {
            y = point2[1];
        } else if (point2[1] == point3[1]) {
            y = point1[1];
        }

        System.out.println(x + " " + y);
    }
}
