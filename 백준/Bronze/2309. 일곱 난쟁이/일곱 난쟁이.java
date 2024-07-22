import java.util.Arrays;
import java.util.Scanner;
 /*
20
7
23
19
10
15
25
8
13
  */
public class Main {
    public static void main(String[] args) {
        int N = 9;
        int[] arr = new int[N];
        int sum = 0;
        int a = 0;
        int b = 0;
        boolean flag = false;
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
        }
        Arrays.sort(arr);

        for (int i = 0 ; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                int except = arr[i] + arr[j];

                if (sum - except == 100) {
                    a = i;
                    b = j;

                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }

        for (int i = 0; i < N ; i++) {
            if (i != a && i != b) {
                System.out.println(arr[i]);
            }
        }
    }
}