import java.io.IOException;
import java.util.Scanner;

public class Main {

    static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        solution();
    }

    private static void solution() throws IOException {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int sum = 0;
        int min = Integer.MAX_VALUE;
        isPrime = new boolean[n+1];
        for (int i = 0; i < isPrime.length; i++) {
            isPrime[i] = true;
        }
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if(isPrime[i]) {
                for (int j = i*i; j <= n; j+=i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int j = m; j <=n; j++) {
            if(isPrime[j]) {
                sum += j;
                if (min > j) {
                    min = j;
                }
            }
        }

        if (sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}
